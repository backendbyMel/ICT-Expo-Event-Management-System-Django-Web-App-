from django import forms
from .models import Photo, Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'section']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']
    