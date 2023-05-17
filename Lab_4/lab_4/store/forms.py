'''from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'producer', 'cost', 'type', 'quantity', 'description', 'image', 'units']'''