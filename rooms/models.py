from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Rooms(models.Model):
    room_type_choices=(("Premium","Premium"),
                        ("Classic","Classic"),
                        ("Cottage","Cottage"))
    room_no=models.CharField(primary_key=True,verbose_name=_('Room No'),max_length=10)
    room_type=models.TextField(choices=room_type_choices,default="Classic",max_length=30)
    room_price=models.IntegerField(default=0)
    # room_status=models.TextField(max_length=200)
    room_available=models.BooleanField(default=True)
    DisplayFields=['room_no','room_type','room_price','room_available']

    def __str__(self):
        return str(self.room_no)