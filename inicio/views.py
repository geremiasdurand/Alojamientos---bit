from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')

def aboutus(request):
    return render(request, "inicio/aboutus.html")

def contacto(request):
    return render(request, "inicio/contacto.html")
