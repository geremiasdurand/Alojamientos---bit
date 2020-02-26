from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2", "first_name", "last_name", "phone"]
