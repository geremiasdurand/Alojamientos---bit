from django.urls import path, include
from . import views

urlpatterns = [
    path('añadir', views.add_res),
]
