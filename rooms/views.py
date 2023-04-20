from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.admin.views.decorators import staff_member_required

import rooms
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView
# Create your views here.

# @staff_member_required
class RoomsCreationView(FormView):
    form_class=RoomsCreationForm
    success_url=reverse_lazy('staffhome')
    template_name='users/room_creation.html'

    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)
    # def post(self,request,*args,**kwargs):
    #     print(request.POST)
    #     return super().post(request,*args,**kwargs)

class RoomsListView(ListView):
    model=Rooms
    template_name="users/roomslist.html"
