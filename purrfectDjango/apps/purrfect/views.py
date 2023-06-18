from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def cargarIndex(request):
    productos = Producto.objects.all()
    return render(request, "index.html",{"prod":productos})

def cargarCaninos(request):
    prodCan = Producto.objects.filter(animal='1')
    return render(request, "caninos.html", {"prod": prodCan})

def cargarMininos(request):
    prodMin = Producto.objects.filter(animal='2')
    return render(request, "mininos.html", {"prod": prodMin})

def cargarAlados(request):
    prodAve = Producto.objects.filter(animal='3')
    return render(request, "alados.html", {"prod": prodAve})

def cargarAcuaticos(request):
    prodAcua = Producto.objects.filter(animal='4')
    return render(request, "acuaticos.html", {"prod": prodAcua})

def cargarAdmin(request):
    productos = Producto.objects.all()
    return render(request, "admin.html", {"Prod": productos})

def cargarCarrito(request):
    return render(request, "carrito.html")

def cargarLogin(request):
    return render(request, "login.html")

def logIn(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(username=username, password=password)
        request.session['username'] = user.username
        request.session['email'] = user.email
        request.session['nombre'] = user.nombre
        request.session['direccion'] = user.direccion
        request.session['telefono'] = user.telefono
        request.session['subscribed'] = user.subscribed
        request.session['tipo'] = user.tipo
        return redirect("/perfil")
    except:
        return redirect("/login")

def cargarPerfil(request):
    return render(request, "perfil.html")

def cargarSuccess(request):
    return render(request, "success.html")

