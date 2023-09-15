from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import ProductForm, ReviewForm
from django.core.exceptions import PermissionDenied
import requests
import random
from docx import Document

def product_list(request, product_type_name = None):
    product_type = None
    types = ProductType.objects.all()
    products = Product.objects.all();

    if product_type_name:
        product_type = get_object_or_404(ProductType, name = product_type_name)
        products = products.filter(type = product_type)

    sort = request.GET.get('sort')
    if sort == 'ascending':
        products = products.order_by('cost')
    elif sort == 'descending':
        products = products.order_by('-cost')

    return render(request, 'store/product/list.html',
                  {
                      'type': product_type,
                      'types': types,
                      'products': products,
                  })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    joke = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]

    return render(request, 'store/product/detail.html', {'product': product,
                                                   'cart_product_form': cart_product_form,
                                                   'joke': joke['setup'] + joke['punchline']})


 
# сохранение данных в бд
def product_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    form = ProductForm()

    if request.method == "POST":
        
        product = Product.objects.create(name=request.POST.get('name'),
                                         producer=Producer.objects.get(id=request.POST.get('producer')),
                                         cost=request.POST.get('cost'),
                                         type=ProductType.objects.get(id=request.POST.get('type')),
                                         quantity=0,
                                         description=request.POST.get('description'),
                                         image=request.FILES.get('image'),
                                         units=request.POST.get('units'))

        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "store/product/create.html", {"form" : form})
    
 
# изменение данных в бд
def product_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        product = Product.objects.get(id=id)
        form = ProductForm(initial={'name':product.name, 'producer':product.producer,
                                    'cost':product.cost, 'type':product.type, 
                                    'description':product.description, 'image':product.image,
                                    'units':product.units})

        if request.method == "POST":
            product.producer=Producer.objects.get(id=request.POST.get('producer'))
            product.cost=request.POST.get('cost')
            product.type=ProductType.objects.get(id=request.POST.get('type'))
            product.description=request.POST.get('description')
            if request.FILES.get('image') != None:
                product.image=request.FILES.get('image')
            product.units=request.POST.get('units')

            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "store/product/edit.html", {"product": product, "form" : form})
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")
     
# удаление данных из бд
def product_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")


def about_company(request) :
    history = History.objects.order_by("year")
    return render(request, "store/store/about_company.html", {"history" : history})

def home_page(request) : 
    partners = Partner.objects.all();
    advertisement = Advertisement.objects.all()
    if len(advertisement) > 3 :
        advertisement = random.sample(Advertisement.objects.all(), 3)

    latest_article = Article.objects.order_by("-date_of_creation").first()

    return render(request, "store/store/home_page.html", {"partners" : partners, "advertisement" : advertisement, 
                                                          "latest_article" : latest_article})

def news(request) :
    articles = Article.objects.all()

    return render(request, "store/store/news.html", {"articles" : articles})

def article_detail(request, id) :
    article = get_object_or_404(Article, id = id)

    return render(request, "store/store/article.html", {"article" : article})

def frequently_questions(request) :
    questions = Question.objects.all()

    return render(request, "store/store/frequently_questions.html", {"questions" : questions})

def workers_info(request) :
    workers_info = WorkerInfo.objects.all()

    return render(request, "store/store/contacts.html", {"workers" : workers_info})

def privacy_policy(request) :
    doc = Document("./media/privacy_policy/privacy_policy.docx")
    html = ""

    for paragraph in doc.paragraphs :
        html += "<p>{0}</p>".format(paragraph.text.replace('\n', '<br>'))

    return render(request, "store/store/privacy_policy.html", {"privacy" : html})

def vacancies(request) :
    vacancies = Vacancy.objects.all()

    return render(request, "store/store/vacancies.html", {"vacancies" : vacancies})

def reviews(request) :
    reviews = Review.objects.all()

    return render(request, "store/store/reviews.html", {"reviews" : reviews})

def create_review(request) :
    form = ReviewForm()
    if request.method == 'POST':
        Review.objects.create(title=request.POST.get('title'), gradle = request.POST.get('gradle'),
                                text = request.POST.get('text'), owner = request.user).save()

        return HttpResponseRedirect('/auth/account')
    elif request.method == 'GET' :
        return render(request, 'store/store/create_review.html', {'form': form})
    
def coupons(request) :
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")
    
    active_coupons = Coupon.objects.filter(active = True)
    deactive_coupons = Coupon.objects.filter(active = False)

    return render(request, "store/store/coupons.html", {"active_coupons" : active_coupons, "deactive_coupons" : deactive_coupons})

def miscellaneous(request) :
    return render(request, "store/store/miscellaneous.html")
