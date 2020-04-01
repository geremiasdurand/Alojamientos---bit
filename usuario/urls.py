from django.urls import path, include
from . import views

urlpatterns = [
    #Se llama la funcion register de views.py
    path('register/', views.register),
    #Se incluyen las urls del auth de django
    path('', include("django.contrib.auth.urls")),
]
