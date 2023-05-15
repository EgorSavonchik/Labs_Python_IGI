from django.db import models
from django.urls import reverse

# Create your models here.

class ProductType(models.Model) :
    
    name = models.CharField(max_length=200,
                             help_text='Enter product type')
    
    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.name)])
    
    def __str__(self) :
        return self.name
    
class Producer(models.Model) :

    name = models.CharField(max_length=200,
                            help_text='Enter prodecer name')
    country = models.CharField(max_length=200,
                               help_text='Enter producer country')

    def get_absolute_url(self):
        return reverse('producer-detail', args=[str(self.id)])

    def __str__(self) :
        return self.name 
    
class Product(models.Model) :

    name = models.CharField(max_length=200)
    producer = models.ForeignKey('Producer',
                                    on_delete = models.SET_NULL,
                                    null = True)
    cost = models.IntegerField()
    type = models.ForeignKey('ProductType', 
                                on_delete = models.SET_NULL,
                                null = True)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    UNITS = (
        ('L', 'liter'),
        ('KG', 'kilogramm'),
        ('PC', 'pieces')
    )
    
    units = models.CharField(max_length=2,
                            choices=UNITS,
                            help_text="units of product")

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.id)])

    def __str__(self) :
        return self.name   

class Client(models.Model) :

    first_name = models.CharField(max_length=200,
                                help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.first_name, self.last_name) 

class Order(models.Model) :
    
    client = models.ForeignKey('Client',
                                on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product',
                                on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date_of_sale = models.DateField(auto_now_add=True)
    date_of_delivery = models.DateField()

    def __str__(self) :
        return '{0}, {1}'.format(self.client, self.product) 
