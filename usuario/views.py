from django.shortcuts import render, redirect
from .forms import RegisterForm

#Funcion que se llama al entrar a /register segun se indica en urls.py
#Esta misma toma como parametro response
def register(response):
    #Del parametro se se verifica si hay un usuario logueado
    if response.user.is_authenticated:
        #Si cumple la condicion anterior se redirige al inicio
        return redirect("/")
    else:
        #Se verifica que el metodo sea POST
        if response.method == "POST":
            #Se guarda el formulario en una variable
            form = RegisterForm(response.POST)
            #Se verifica si el formulario es valido y luego se guarda a la base de datos
            if form.is_valid():
                form.save()
            #Se redirige a la pagina de login
            return redirect("/login")
        else:
            form = RegisterForm()
        #Renderiza el HTML y le da valores al formulario
        return render(response, "usuario/register.html", {"form":form})
