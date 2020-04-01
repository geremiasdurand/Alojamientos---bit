from django.urls import path
from . import views

app_name = 'inicio'
urlpatterns = [
    #Se llaman las funciones de views.py y se les asignan una direcion
    path("", views.index),
    path("aboutus", views.aboutus),
    path("contacto", views.contacto),
]
