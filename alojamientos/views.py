from django.shortcuts import render
from .forms import ResidenciaForm

# Create your views here.
def add_res(response):
    if response.method == "POST":
        form = ResidenciaForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/residencia_añadida")
    else:
        form = ResidenciaForm()
    return render (request, "alojamientos/añadir.html", {"form":form})
    #if response.user.is_authenticated:

    #else:
    #    return redirect("usuario/register.html")
