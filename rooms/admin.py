from django.contrib import admin
from .models import *
# admin.site.register(Rooms)

@admin.register(Rooms)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=Rooms.DisplayFields

# Register your models here.
