from django import forms
from .models import Contacto

#Formulario de creacion de contacto que hereda de ModelForm
class ContactoForm(forms.ModelForm):

    class Meta:
        #Modelo a utilizar es el creado en models.py
        model = Contacto
        #Campos que aparecen en el form
        fields = ("nombre", "email", "mensaje")
