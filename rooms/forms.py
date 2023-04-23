from django import forms
from .models import *

class RoomsCreationForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields="__all__"

class SampleForm(forms.Form):
    name=forms.CharField(max_length=10)
    age=forms.IntegerField()
