from django import forms
from .models import Challenger

class ChallengerPhotoForm(forms.ModelForm):
    class Meta:
        model = Challenger
        fields = ['photo']