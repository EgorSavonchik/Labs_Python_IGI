from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('about_company/', views.about_company, name='about_company'),
     path('home_page', views.home_page, name='home_page'),
     path('news', views.news, name = 'news'),
     path('article/<int:id>', views.article_detail, name = 'article-detail'),
     path('questions' , views.frequently_questions , name='frequently_questions'),
     path('contacts', views.workers_info, name="contacts"),
     path('privacy-policy', views.privacy_policy, name ="privacy_policy"),
     path('reviews', views.reviews , name ='reviews'),
     path('review/create', views.create_review, name='create_review'),
     path('vacancies', views.vacancies, name = 'vacancies'),
     path('cupons', views.coupons, name = 'coupons'),
     path('miscellaneous', views.miscellaneous, name = 'miscellaneous'),
     path('<int:id>', views.product_detail,
          name='product_detail'),
     path("create/", views.product_create),
     path("edit/<int:id>/", views.product_edit),
     path("delete/<int:id>/", views.product_delete),
     
     path('<str:product_type_name>/', views.product_list,
          name='product_list_by_category'
          ),
]