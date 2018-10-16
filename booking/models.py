from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# added comment here
#git pull origin master
class City(models.Model):
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


class Moviedetails(models.Model):
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
    image=models.ImageField(upload_to='media',
        null=True,
        blank=True,
        width_field='widht_field',
        height_field='height_field'
        )
    widht_field=models.PositiveIntegerField(default=0)
    height_field=models.PositiveIntegerField(default=0)
    description=models.TextField()
    name=models.CharField(max_length=50)
    review=models.TextField()
    rating=models.PositiveIntegerField()

    def __str__(self):
        return self.name  + ' Category ' + self.category + ' Rating ' + self.rating



class Payment(models.Model):
    payment_options=('CreditCard','PayTM')
    timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)



#class PaymentDetails(models.Model):
