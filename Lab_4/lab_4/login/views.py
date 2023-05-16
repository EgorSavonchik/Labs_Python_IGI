from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


class RegisterFormView(FormView) :
    form_class = UserCreationForm
    success_url = '/'

    template_name = 'register.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super(RegisterFormView, self).form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        return super(RegisterFormView, self).form_invalid(form)
    
class LoginFormView(FormView) :
    form_class = AuthenticationForm

    template_name = 'login.html'

    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        self.user = form.get_user()

        login(self.request, self.user)    
        return super(LoginFormView, self).form_valid(form)
        
class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')