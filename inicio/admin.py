from django.contrib import admin
from .models import Contacto
from django.contrib.auth.admin import UserAdmin

#Clase que define que datos aparecen, cuales son los cirterios de busqueda y cuales se pueden modificar
#en el sitio de django
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "is_answered",)
    search_fields = ("email", "nombre", "is_answered")
    readonlyfields = ("nombre", "email", "mensaje",)
    ordering = ('id',)
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

#Se registra para que aparezca en el sitio admin de django
admin.site.register(Contacto, ContactoAdmin)
