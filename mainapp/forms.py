from django import forms
from . import models
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'password1', 'password2')


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = models.User
        fields = ('username', 'password')