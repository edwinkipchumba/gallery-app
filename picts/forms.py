from django import forms
from django.forms import ModelForm
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

CATEGORIES =( 
    ("1", "Cars"), 
    ("2", "Food"), 
    ("3", "Travel"),  
    ("4", "People"), 
    ("5", "Animals"), 
    ("6", "Nature"), 
    ("7", "Sports"), 
) 