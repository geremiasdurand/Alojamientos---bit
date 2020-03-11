from from django import forms
from django.forms import ModelForm
from .models import Alojamiento


class ResidenciaForm(ModelForm):
    class Meta:
        model = Alojamiento
        fields = ["title", "description", "location"]
