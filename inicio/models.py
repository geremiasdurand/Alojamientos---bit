from django.db import models

#Modelo de Contacto con el que se basa para crear la tabla de la base de datos
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()
    is_answered = models.BooleanField(default=False)
