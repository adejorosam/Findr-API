from django.contrib.auth.backends import ModelBackend
from .models import User
from django.http import Http404
from rest_framework import response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


class LoginBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        phone_number= kwargs['phone_number']
        try:
            return User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
           