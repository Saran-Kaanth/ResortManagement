from django import forms
from .models import *

class RoomsCreationForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields="__all__"

        