from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from cart.forms import CartAddProductForm

def product_list(request, product_type_name = None):
    product_type = None
    types = ProductType.objects.all()
    products = Product.objects.all();

    if product_type_name:
        product_type = get_object_or_404(ProductType, name = product_type_name)
        products = products.filter(type = product_type)

    return render(request, 'store/product/list.html',
                  {
                      'type': type,
                      'types': types,
                      'products': products
                  })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product/detail.html', {'product': product,
                                                   'cart_product_form': cart_product_form})