from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Alojamiento, Comentario
from .forms import AlojamientoForm, ComentarioForm
from django.shortcuts import redirect
from django.contrib import messages


def alojamiento_list(request):
    #Se utiliza un QuerySet para obtener los alojamientos
    #y se los ordena segun su fecha de creacion
    alojamientos = Alojamiento.objects.all().order_by('-fecha_de_creacion')
    #Se renderiza el HTML y se envia el objeto de alojamientos para ser utilizados
    return render(request, 'alojamientos/alojamiento_list.html', {'alojamientos': alojamientos})

#Se obtiene como parametro la pk del alojamiento
def alojamiento_detail(request, pk):
    #Se obtiene el objeto si es que existe segun la pk que tenemos como parametro inicial
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    #Se envia el objeto y se renderiza el HTML
    return render(request, 'alojamientos/alojamiento_detail.html', {'alojamiento': alojamiento})

def alojamiento_new(request):
    #Se verifica que el metodo sea POST
    if request.method == "POST":
        #Se guarda el formulario en un objeto
        form = AlojamientoForm(request.POST)
        #Se verifica si el formulario es valido y luego se guarda a la base de datos
        if form.is_valid():
            alojamiento = form.save(commit=False)
            #Se le da el valor al autor basandose en el usuario que esta logueado
            alojamiento.autor = request.user
            alojamiento.save()
            #Redirecciona al link con el parametro de pk como valor
            return redirect('/alojamientos', pk=alojamiento.pk)
    else:
        form = AlojamientoForm()
    #Renderiza el HTML y le da valores al formulario si es que ya tenia
    return render(request, 'alojamientos/alojamiento_add.html', {'form': form})

def añadir_comentario(request, pk):
    #Se obtiene el objeto si es que existe segun la pk que tenemos como parametro inicial
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    #Se verifica que el metodo sea POST
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        #Se verifica si el formulario es valido y luego se guarda a la base de datos
        if form.is_valid():
            comentario = form.save(commit=False)
            #Se asigna el alojamiento segun la pk que se tiene de parametro inicial
            comentario.alojamiento = alojamiento
            #Se le da el valor al autor basandose en el usuario que esta logueado
            comentario.autor = request.user
            comentario.save()
            #Redirecciona al link con el parametro de pk como valor
            return redirect('alojamiento_detail', pk=alojamiento.pk)
    else:
        form = ComentarioForm()
    #Renderiza el HTML y le da valores al formulario si es que ya tenia
    return render(request, 'alojamientos/añadir_comentario.html', {'form': form})

def eliminar_comentario(request, pk):
    #Se obtiene el objeto si es que existe segun la pk que tenemos como parametro inicial
    comentario = get_object_or_404(Comentario, pk=pk)
    #Se elimina el objeto de la base de datos
    comentario.delete()
    #Redirecciona al link con el parametro de pk como valor
    return redirect('alojamiento_detail', pk=comentario.alojamiento.pk)

def alojamiento_edit(request, pk):
    #Se obtiene el objeto si es que existe segun la pk que tenemos como parametro inicial
    instancia = Alojamiento.objects.get(pk=pk)
    #Se carga un objeto teniendo en cuenta el formulario y la base datos
    #Se utiliza para obtener solo los datos del formulario
    form = AlojamientoForm(instance=instancia)
    #Se verifica que el metodo sea POST
    if request.method == "POST":
        #Se le da valor al formulario segun el objeto obtenido
        form = AlojamientoForm(request.POST, instance=instancia)
        #Se verifica si el formulario es valido y luego se guarda a la base de datos
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            #Se envia un mensaje
            messages.success(request, 'Editado con exito')
    #Renderiza el HTML y le da valores al formulario si es que ya tenia
    return render(request, "alojamientos/alojamiento_edit.html", {'form': form})

def alojamiento_delete(request, pk):
    #Se obtiene el objeto segun la pk que tenemos como parametro inicial
    instancia = Alojamiento.objects.get(pk=pk)
    #Se elimina el objeto de la base de datos
    instancia.delete()
    #Redirecciona al link
    return redirect("alojamiento_list")
