from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_typing_staff = forms.BooleanField(required=False, label="Typing Sprint Staff")
    is_cashier = forms.BooleanField(required=False, label="Cashier")
    is_uploader = forms.BooleanField(required=False, label="Photo Uploader")
    is_downloader = forms.BooleanField(required=False, label="Photo Downloader")

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'is_typing_staff',
                  'is_cashier',
                  'is_uploader',
                  'is_downloader',]