from django.db import models
from django.utils import timezone
from django.contrin.auth.models import User
# Create your models here.
# added comment here
class city(models.Model):
    city_choice=(
    ('DELHI','Delhi'),
    ('MUMBAI','Mumbai'),
    ('HYDERABAD','Hyderabad'),
    ('BENGALURU','Bengaluru'),
    ('KOLKATA','Kolkata'),
    ('CHENNAI','Chennai'),
    )
    city_id=models.ForeignKey('auth_user',on_delete=models.CASCADE)
    numberoftheatres=models.IntegerField(default=0)

class theatre(models.Model):
    theatre_name=models.CharField(max_length=200)
    theatre_city=models.CharField(max_length=50)
    theatre_address=models.CharField(max_length=400)
    showtimimgs=models.

class moviedetails(models.Model):
    category=(
    ('ACTION','Action'),
    ('ROMANTIC','Romantic'),
    ('THRILLER','Thriller'),
    ('HORROR','Horror'),
    ('COMEDY','Comedy')
    )
    certification=(
    ('U','Can be seen by all'),
    ('A','Adults only'),
    ('UA','Accompanied by Parents'),
    ('S','Special Category'),
    )
    language=(
    ('ENGLISH','English'),
    ('HINDI','Hindi'),
    ('TAMIL','Tamil'),
    ('KANNADA','Kannada'),
    )
    image=models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        width_field='widht_field',
        height_field='height_field'
        )
    widht_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    description=models.TextField()
    name=models.CharField(max_length=50)
    review=models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return self.name  + ' Category ' + self.category + ' Rating ' + self.rating

class userdetails(models.Model):
    user_id=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    name=models.CharField(max_length)
    bookinghistory=
    notifications=


class paymentdetails(models.Model):
    payment_options=('CreditCard','PayTM')
    timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)



class theaterseat(models.Model):
    seats=(
    ('PLATINUM','Platinum'),
    ('GOLD','Gold'),
    ('SILVER','Silver'),
    ('DIAMOND','Diamond')
    )
    seatsavailaible=models.IntegerField()
    timings=models.DateTimeField(blank=True,null=True)


class bookedseatdetails(models.Model):

class paymentdetails(models.Model):
