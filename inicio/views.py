from django.shortcuts import render
from alojamientos.models import Alojamiento as Alojamiento
from .forms import ContactoForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    alojamientos = Alojamiento.objects.all().filter(is_sponsored=True).order_by('-fecha_de_creacion')
    return render(request, 'inicio/index.html', {'alojamientos': alojamientos})

def aboutus(request):
    return render(request, "inicio/aboutus.html")

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()
            return redirect('/contacto')
    else:
        form = ContactoForm()
    return render(request, 'inicio/contacto.html', {'form': form})
