from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
#from django.contrib.auth.models import User



# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',max_length=60)
    phone_number = models.CharField('phone_number',max_length=11,unique=True)
    is_admin = models.BooleanField('staff_status',max_length=6, default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    #key = models.CharField(max_length=100, unique=True, blank=True
    objects = models.Manager()
    USERNAME_FIELD = 'phone_number'
   

    def __str__(self):
        return self.username

class Apartment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    house_address = models.CharField('house_address',max_length=10000)
    #apartment_categories = models.ForeignKey('ApartmentCategory',on_delete=models.CASCADE)
    house_name = models.CharField('house_name',max_length=60)
    house_pic = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)
    price = models.CharField('price',max_length=60)
    total_rooms = models.CharField('total_rooms', max_length=100),
    choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    isFurnished = models.CharField('furnished',max_length=50,choices=choices)
    isParkingSpace = models.CharField('parkingspace',max_length=70,choices=choices)
    isAvailable = models.CharField('available', max_length=100,choices=choices)
    isFenced = models.CharField('fenced', max_length=100, choices=choices)
    isHaveWater = models.CharField('water', max_length=100,choices=choices)
    isNewHouse = models.CharField('new',max_length=80,choices=choices)
    isNegotiable = models.CharField('bargained', max_length=80,choices=choices)
    date_posted = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    
    def __str__(self):
        return self.house_name








