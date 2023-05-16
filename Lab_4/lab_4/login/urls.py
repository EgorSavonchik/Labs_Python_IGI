from . import views
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view())
]