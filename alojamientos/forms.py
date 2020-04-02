from django import forms
from .models import Alojamiento, Comentario

#Formulario de creacion de Alojamiento que hereda de ModelForm
class AlojamientoForm(forms.ModelForm):

    class Meta:
        #Modelo a utilizar es el creado en models.py
        model = Alojamiento
        #Campos que aparecen en el form
        fields = ("titulo", "barrio", "direccion", "telefono", "texto",)


#Formulario de creacion de Comentario que hereda de ModelForm
class ComentarioForm(forms.ModelForm):

    class Meta:
        #Modelo a utilizar es el creado en models.py
        model = Comentario
        #Campos que aparecen en el form
        fields = ("texto",)
