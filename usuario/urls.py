from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register),
    path('', include("django.contrib.auth.urls")),
]
