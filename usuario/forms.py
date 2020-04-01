from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group


#Formulario de creacion de usuario que hereda de UserCreationForm
class RegisterForm(UserCreationForm):
    #Se agrega el campo de phone ya que el modelo User de django no viene con este campo.
    phone = forms.CharField()
    class Meta:
        #Modelo a utilizar es User de django
    	model = User
        #Campos que aparecen en el form
    	fields = ["username", "email", "password1", "password2", "first_name", "last_name", "phone"]
