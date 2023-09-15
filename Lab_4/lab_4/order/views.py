from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from store.models import Coupon
from .models import CustomUser
from .models import Order
from django.core.exceptions import PermissionDenied
from datetime import datetime
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

def order_create(request):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    if request.method == 'POST':        
        order = Order.objects.create(client = request.user)
        
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount

            Coupon.objects.filter(id = order.coupon.id).update(active = False)
        

        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['cost'],
                                        quantity=item['quantity'])
            item['product'].purchase_count += item['quantity']
            item['product'].save()

        order.total_cost = order.get_total_cost()
        order.save()

        # очистка корзины
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': order})
    
    return render(request, 'order/create.html',
                  {'cart': cart})

@require_POST
def coupon_apply(request):

    try:
        coupon = coupon = Coupon.objects.get(code=request.POST.get('coupon_code'),
                                    date_of_creation__lte = datetime.now().date(),
                                    active=True)
        request.session['coupon_id'] = coupon.id
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None

    return redirect('cart:cart_detail')