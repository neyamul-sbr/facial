from django import forms
from .models import *

class ImageUpForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    age = forms.CharField(label='your age', max_length= 10)

    