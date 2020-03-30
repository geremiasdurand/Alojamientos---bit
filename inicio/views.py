from django.shortcuts import render
from alojamientos.models import Alojamiento as Alojamiento

# Create your views here.
def index(request):
    alojamientos = Alojamiento.objects.all().filter(is_sponsored=True).order_by('-fecha_de_creacion')
    return render(request, 'inicio/index.html', {'alojamientos': alojamientos})

def aboutus(request):
    return render(request, "inicio/aboutus.html")

def contacto(request):
    return render(request, "inicio/contacto.html")
