from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class RegistrationForm(UserCreationForm):
    pass