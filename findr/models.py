from django.db import models
#from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone

# Create your models here.

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(models.Model):
    username = models.CharField('username',max_length=30)
    phone_number = models.CharField('phone_number',max_length=20,unique=True)
    is_admin = models.BooleanField('staff_status',max_length=6)
    date_joined = models.DateTimeField(default=timezone.now)

class House(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
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
    isNegotiable = models.CharField('new', max_length=80,choices=choices)








