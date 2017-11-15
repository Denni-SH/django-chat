from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth import models
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
# from channels. import channel_session_user_from_http

class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpCreateView(generic.CreateView):
    template_name = "sign_up.html"
    model = models.User
    form_class = forms.CustomUserCreationForm
    success_url = "/"


class MyLoginView(LoginView):
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    pass
