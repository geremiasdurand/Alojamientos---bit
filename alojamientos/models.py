from django.db import models
from django.utils import timezone

#Modelo de Alojamiento con el que se basa para crear la tabla de la base de datos
class Alojamiento(models.Model):

    BARRIOS = (
    ('AG', 'Aguada'),
    ('BS', 'Barrio Sur'),
    ('BU', 'Buceo'),
    ('CS', 'Carrasco'),
    ('CT', 'Centro'),
    ('CE', 'Cerro'),
    ('CV', 'Ciudad Vieja'),
    ('CN', 'Cordón'),
    ('CR', 'Capurro'),
    ('LU', 'La Unión'),
    ('MÑ', 'Maroñas'),
    ('PR', 'Parque Rodó'),
    ('PÑ', 'Peñarol'),
    ('PC', 'Pocitos'),
    ('PG', 'Punta Gorda'),
    ('OT', 'Pocitos')
    )

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    barrio = models.CharField(max_length=2, choices=BARRIOS)
    direccion = models.CharField(max_length=50, default="Sin dirección")
    titulo = models.CharField(max_length=45)
    telefono = models.DecimalField(max_digits=15, decimal_places=0)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    is_sponsored = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'gallery', default = 'gallery/static/images/default.png')

    def __str__(self):
        return self.titulo


#Modelo de Comentario con el que se basa para crear la tabla de la base de datos
class Comentario(models.Model):
    alojamiento = models.ForeignKey("alojamientos.Alojamiento", on_delete=models.CASCADE, related_name='comentario')
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto
