from django.contrib import admin

from .models import Product, Producer, ProductType, Client, Order
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin) :
    list_display = ['name', 'producer', 'cost', 'type', 'units']

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin) :
    list_display = ['name', 'country']

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin) :
    list_display = ['name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin) :
    list_display = ['first_name', 'last_name', 'date_of_birth',
                    'email', 'phone_number']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin) :
    list_display = ['client', 'product', 'quantity', 'date_of_delivery']
