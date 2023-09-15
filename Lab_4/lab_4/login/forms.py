from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime

def validate_age(value):
    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    print(today.year)
    print(value.year)
    print(age)
    if int(age) < 18:
        raise ValidationError("Вы должны быть старше 18 лет.")

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=200,
                                help_text='Enter first name',
                                validators=[RegexValidator(
            regex=r'^[\w]+$',
            message='Name must consist of letters',
        )])
    last_name = forms.CharField(max_length=200,
                                help_text='Enter last name',
                                validators=[RegexValidator(
            regex=r'^[\w]+$',
            message='Name must consist of letters',
        )])
    date_of_birth = forms.DateField(validators=[validate_age], 
                                    help_text="Format YYYY-MM-DD",
                                    error_messages={
            'invalid': 'Format YYYY-MM-DD',
        })
    phone_number = forms.CharField(max_length=50,
                                    help_text='Enter phone number',
                                    validators=[RegexValidator(
            regex=r'^(\+375 \([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
            message='Format +375 (XX) XXX-XX-XX',
        )])
    
    class Meta:
        model = CustomUser
        fields = {'username', 'email', 'first_name', 
                  'last_name', 'date_of_birth', 
                  'phone_number', 'password1', 
                  'password2'
        }

    def save(self, commit: bool = ...) -> Any:
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.phone_number = self.cleaned_data['phone_number']

        if commit:
            user.save()
        
        return user
    