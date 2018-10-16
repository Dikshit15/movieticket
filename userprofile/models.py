from django.db import models
from django.utils import timezone

# Create your models here.

class Userdetails(models.Model):
    user_id=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    name=models.CharField(max_length)
    bookinghistory=
    notifications=
