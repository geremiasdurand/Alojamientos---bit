from django.contrib import admin
from .models import Alojamiento, Comentario

#Se registra para que aparezca en el sitio admin de django
admin.site.register(Alojamiento)
admin.site.register(Comentario)
