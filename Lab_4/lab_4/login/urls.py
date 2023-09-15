from . import views
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('account', views.AccountView.as_view() , name='personal_account'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]