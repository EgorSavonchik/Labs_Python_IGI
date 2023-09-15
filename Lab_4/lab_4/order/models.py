from django.db import models
from store.models import Product, Coupon
from login.models import CustomUser
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

class Order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    coupon = models.ForeignKey(Coupon,
                                on_delete=models.SET_DEFAULT,
                                default=None,
                                null=True,
                                blank=True)
    discount = models.IntegerField(default=0,
                                        validators=[MinValueValidator(0),
                                                    MaxValueValidator(100)])
    total_cost = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))
    
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    # фатальная ошибка, нельзя ставить на продукт каскад, т. к. создал ордер неделю назад, сейчас удалил
    # товар - старый ордер поменяется, лучше добавить в продукт поле ис_делитед
    # чтобы он оставался в бд но нигде не отображался
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity