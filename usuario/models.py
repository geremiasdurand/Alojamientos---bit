from django.db import models

# Create your models here.
class student(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
