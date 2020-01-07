'''from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Apartment

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number']
'''