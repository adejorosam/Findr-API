from django.contrib import admin
from .models import Apartment, User, Image


# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass
'''
class ApartmentCategoryAdmin(admin.ModelAdmin):
    pass
'''

admin.site.register(Apartment)
admin.site.register(User)
admin.site.register(Image)

#admin.site.register(ApartmentCategory)
