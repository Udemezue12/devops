from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
# from django.conf import settings

from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


# Create a User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Authenicate a User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
