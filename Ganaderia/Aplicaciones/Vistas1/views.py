from django.shortcuts import render,redirect

def inicio(request):
    return render(request,'index.html')

def categorias(request):
    return render(request,'categorias.html')

# Create your views here.
