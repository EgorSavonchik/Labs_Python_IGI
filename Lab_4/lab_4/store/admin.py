from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin) :
    list_display = ['name', 'producer', 'image', 'cost', 'type', 'units']
    list_filter = ['producer', 'type']

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin) :
    list_display = ['name', 'country']

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin) :
    list_display = ['name']
    
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Advertisement._meta.get_fields()]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Article._meta.get_fields()]

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'date_of_creation', 'active')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Partner._meta.get_fields()]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Question._meta.get_fields()]
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Review._meta.get_fields()]

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in Vacancy._meta.get_fields()]

@admin.register(WorkerInfo)
class WorkerInfoAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in WorkerInfo._meta.get_fields()]

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin) :
    list_display =  [field.name for field in History._meta.get_fields()]
