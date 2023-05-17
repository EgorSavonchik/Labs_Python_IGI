from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

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


 
# сохранение данных в бд
def product_create(request):
    if request.method == "POST":
        product = Product.objects.create(name=request.POST.get('name'),
                                         producer=request.POST.get('producer'),
                                         cost=request.POST.get('cost'),
                                         type=request.POST.get('type'),
                                         quantity=0,
                                         description=request.POST.get('description'),
                                         image=request.POST.get('image'),
                                         units=request.POST.get('units'))

        product.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def product_edit(request, id):
    form = 
    try:
        product = Product.objects.get(id=id)
 
        if request.method == "POST":
            product.producer=request.POST.get('producer')
            product.cost=request.POST.get('cost')
            product.type=request.POST.get('type')
            product.quantity=request.POST.get('quantity')
            product.description=request.POST.get('description')
            product.image=request.POST.get('image')
            product.units=request.POST.get('units')

            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "store/product/edit.html", {"product": product})
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")
     
# удаление данных из бд
def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")