from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:product_type_name>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>', views.product_detail,
         name='product_detail')
]