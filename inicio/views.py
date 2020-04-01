from django.shortcuts import render
from alojamientos.models import Alojamiento as Alojamiento
from .forms import ContactoForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    #Se utiliza un QuerySet para obtener los alojamientos que tienen son sponsors (is_sponsored==True)
    #Y se los ordena segun su fecha de creacion
    alojamientos = Alojamiento.objects.all().filter(is_sponsored=True).order_by('-fecha_de_creacion')
    #Se renderiza el HTML y se devuelve un objeto para que se utilice
    return render(request, 'inicio/index.html', {'alojamientos': alojamientos})

def aboutus(request):
    #Se renderiza el HTML
    return render(request, "inicio/aboutus.html")

def contacto(request):
    #Se verifica que el metodo sea POST
    if request.method == "POST":
        #Se guarda el formulario en una variable
        form = ContactoForm(request.POST)
        #Se verifica si el formulario es valido y luego se guarda a la base de datos
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.save()
            #Se redirige a la pagina de de contacto nuevamente
            return redirect('/contacto')
    else:
        form = ContactoForm()
    #Renderiza el HTML y le da valores al formulario si es que ya tenia
    return render(request, 'inicio/contacto.html', {'form': form})
