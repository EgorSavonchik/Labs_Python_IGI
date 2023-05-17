from django.shortcuts import render
from .models import OrderItem
#from .forms import OrderCreateForm
from cart.cart import Cart
from store.models import Client
from .models import Order

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':        
        order = Order.objects.create(client = Client.objects.filter(email=request.user.email).first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['cost'],
                                        quantity=item['quantity'])
        # очистка корзины
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': order})
    
    return render(request, 'order/create.html',
                  {'cart': cart})