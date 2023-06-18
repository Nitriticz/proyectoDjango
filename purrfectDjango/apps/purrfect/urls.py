from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarIndex),
    path('index',views.cargarIndex),
    path('caninos',views.cargarCaninos),
    path('mininos',views.cargarMininos),
    path('alados',views.cargarAlados),
    path('acuaticos',views.cargarAcuaticos),
    path('admin',views.cargarAdmin),
    path('carrito',views.cargarCarrito),
    path('login',views.cargarLogin),
    path('perfil',views.cargarPerfil),
    path('success',views.cargarSuccess),
    path('admin', views.cargarAdmin),
    path('loginForm',views.logIn)
]