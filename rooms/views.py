from queue import Empty
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
import rooms
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Rooms
# Create your views here.

# @staff_member_required
class RoomsCreationView(FormView):
    form_class=RoomsCreationForm
    success_url=reverse_lazy('staffhome')
    template_name='users/room_creation.html'


    def form_valid(self, form) :
        form.save()
        message="Data Saved Successfully"
        form=self.form_class
        return render(self.request,"users/room_creation.html",locals())

    def form_invalid(self, form):
        error_message="Check with your data"
        form=self.form_class
        return render(self.request,"users/room_creation.html",locals())
        
        # return super().form_valid(form)
    # def post(self,request,*args,**kwargs):
    #     print(request.POST)
    #     return super().post(request,*args,**kwargs)

class RoomsListView(ListView):
    model=Rooms
    template_name="users/roomslist.html"
    context_object_name="rooms_list"

    def get_queryset(self) :
        print("hii")
        rooms_list=Rooms.objects.raw("select * from rooms_Rooms limit 2")
        # print(rooms_list)
        for room in Rooms.objects.raw("select * from rooms_Rooms"):
            print(room)
        return rooms_list

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        print(not self.request.GET)
        context=super(RoomsListView,self).get_context_data(**kwargs)
        context['form']=RoomsSearchFrom()
        context['rooms_list']=Rooms.objects.raw("select * from rooms_Rooms  where room_type='Classic' and room_no='C324'")
        if not self.request.GET:
            context['name']='saran'
        print(context)
        return context


    # def get(self, request, *args, **kwargs) :
    #     print(request.GET)
    #     if request.GET.get('email') is None:
    #         return super().get(request, *args, **kwargs)
    #         # return render(self.request,"users/roomslist.html",locals())     
    #     else:    
    #         return render(self.request,"users/roomslist.html",locals())


class SampleView(FormView):
    form_class=SampleForm
    template_name: str='users/sample.html'

    def post(self, request,*args,**kwargs):
        print(request.POST)
        form=self.form_class()
        name=request.POST['name']
        age=request.POST['age']
        return render(self.request,"users/sample.html",locals())
