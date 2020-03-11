from django.db import models

# Create your models here.
class Alojamiento(models.Model):
    title = models.CharField(max_length=25)
    #imagen = models.ImageField()
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=25)

    def __str__(self):
        return self.title
