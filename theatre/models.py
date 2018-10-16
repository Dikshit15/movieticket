from django.db import models
from django.utils import timezone
# Create your models here.

class Theatre(models.Model):
    theatre_name=models.CharField(max_length=200)
    theatre_city=models.CharField(max_length=50)
    theatre_address=models.CharField(max_length=400)
    #showtimimgs=(
    #'9:30-12:30'
    #)



class Theaterseat(models.Model):
    seats=(
    ('PLATINUM','Platinum'),
    ('GOLD','Gold'),
    ('SILVER','Silver'),
    ('DIAMOND','Diamond')
    )
    seatsavailaible=models.IntegerField()
    #timings=models.DateTimeField(blank=True,null=True)


class Bookedseatdetails(models.Model):
