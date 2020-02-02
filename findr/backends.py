from django.contrib.auth.backends import ModelBackend
from .models import User
from django.http import Http404

class LoginBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        phone_number= kwargs['username']
        try:
            return User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise Http404
           