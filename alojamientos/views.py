from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Alojamiento, Comentario
from .forms import AlojamientoForm, ComentarioForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def alojamiento_list(request):
    alojamientos = Alojamiento.objects.all().order_by('-fecha_de_creacion')
    return render(request, 'alojamientos/alojamiento_list.html', {'alojamientos': alojamientos})

def alojamiento_detail(request, pk):
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    #comentarios = Comentario.objects.filter(alojamiento_id=pk).order_by('-fecha_de_creacion')
    return render(request, 'alojamientos/alojamiento_detail.html', {'alojamiento': alojamiento})

def alojamiento_new(request):
    if request.method == "POST":
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.autor = request.user
            alojamiento.save()
            return redirect('/alojamientos', pk=alojamiento.pk)
    else:
        form = AlojamientoForm()
    return render(request, 'alojamientos/alojamiento_add.html', {'form': form})

def añadir_comentario(request, pk):
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.alojamiento = alojamiento
            comentario.autor = request.user
            comentario.save()
            return redirect('alojamiento_detail', pk=alojamiento.pk)
    else:
        form = ComentarioForm()
    return render(request, 'alojamientos/añadir_comentario.html', {'form': form})

def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    return redirect('alojamiento_detail', pk=comentario.alojamiento.pk)

def alojamiento_edit(request, pk):
    instancia = Alojamiento.objects.get(pk=pk)
    form = AlojamientoForm(instance=instancia)
    if request.method == "POST":
        form = AlojamientoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            messages.success(request, 'Editado con exito')

    return render(request, "alojamientos/alojamiento_edit.html", {'form': form})

def alojamiento_delete(request, pk):
    instancia = Alojamiento.objects.get(pk=pk)
    instancia.delete()

    return redirect("alojamiento_list")
