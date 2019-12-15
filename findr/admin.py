from django.contrib import admin
from .models import House,User

# Register your models here.

class HouseAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(House)
admin.site.register(User)
