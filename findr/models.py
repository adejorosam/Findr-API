from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
from django.utils import timezone


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',max_length=60, unique=True)
    phone_number = models.CharField('phone_number',max_length=11,unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    #last_login = LastSeen.objects.when(user=user)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin '
                                               'site.')
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
   

    def __str__(self):
        return self.username

class Apartment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    house_address = models.CharField('house_address',max_length=10000)
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
    isNegotiable = models.CharField('Negotiable', max_length=80,choices=choices)
    date_posted = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    
    def __str__(self):
        return self.house_name








