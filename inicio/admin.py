from django.contrib import admin
from .models import Contacto
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "is_answered",)
    search_fields = ("email", "nombre", "is_answered")
    readonlyfields = ("nombre", "email", "mensaje",)
    ordering = ('id',)
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Contacto, ContactoAdmin)
