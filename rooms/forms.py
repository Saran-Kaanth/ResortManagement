from django import forms
from .models import *
from django.forms.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
import datetime

class RoomsCreationForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields="__all__"

class SampleForm(forms.Form):
    name=forms.CharField(max_length=10)
    age=forms.IntegerField()

class RoomsSearchFrom(forms.Form):
    room_type_choices=(("Premium","Premium"),
                        ("Classic","Classic"),
                        ("Cottage","Cottage"))
    check_in=forms.DateField(widget=forms.widgets.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'style': 'max-width: 300px;',
                'class':'form-control'
                }))
    check_out=forms.DateField(widget=forms.widgets.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'style': 'max-width: 300px;',
                'class':'form-control'
                }))
    room_type=forms.ChoiceField(choices=room_type_choices)

