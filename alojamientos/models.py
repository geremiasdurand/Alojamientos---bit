from django.db import models
from django.utils import timezone

# Create your models here.
class Alojamiento(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    alojamiento = models.ForeignKey("alojamientos.Alojamiento", on_delete=models.CASCADE, related_name='comentario')
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto
