from django.contrib import admin
from .models import Order, OrderItem



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'created', 'coupon', 'discount')
    list_filter = ['created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)