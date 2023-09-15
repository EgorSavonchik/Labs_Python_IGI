from django import forms
from .models import Product, Review, GRADLE_CHOICES


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'producer', 'cost', 'type', 'description', 'image', 'units']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text', 'gradle']
        widgets = {'gradle' : forms.Select(choices=GRADLE_CHOICES) }