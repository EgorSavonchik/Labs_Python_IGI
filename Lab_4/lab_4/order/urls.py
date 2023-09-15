
from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('coupon', views.coupon_apply, name="coupon_apply")
]