from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .forms import UserCreateForm 
import requests


class RegisterFormView(FormView) :
    form_class = UserCreateForm
    success_url = '/auth/login/'

    template_name = 'register.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()

        return super(RegisterFormView, self).form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        return super(RegisterFormView, self).form_invalid(form)
    
class LoginFormView(FormView) :
    form_class = AuthenticationForm
    
    '''quote = requests.get('https://favqs.com/api/qotd')

    if(quote != None) :
        quote = quote.json()
    else :
        quote = "Not Found"'''
    
    template_name = 'login.html'

    def get(self, request) :
        return render(request, 'login.html', context={'form' : self.form_class()}) #'quote' : self.quote['quote']['body']'''})

    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        self.user = form.get_user()

        login(self.request, self.user)    
        return super(LoginFormView, self).form_valid(form)
        
class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')
    
class AccountView(View) :
    def get(self, request):
        return render(request, 'personal_account.html')