from django.shortcuts import render,redirect

def inicio(request):
    return render(request,'index.html')

def categorias(request):
    return render(request,'categorias.html')

def seccion(request):
    return render(request, 'seccion.html')

def iniciar_seccion(request):
    return render(request,'iniciar_seccion.html')

def registrarse(request):
    return render(request,'registrarse.html')

# Create your views here.
