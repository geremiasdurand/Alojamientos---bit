from django.urls import path
from . import views

app_name = 'inicio'
urlpatterns = [
    path("", views.index),
    path("aboutus", views.aboutus),
    path("contacto", views.contacto),
]
