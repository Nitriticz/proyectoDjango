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
    path('editUser',views.editUser),
    path('addSub', views.addSub),
    path('delSub', views.delSub),
    path('pago',views.pago),
    path('success',views.cargarSuccess),
    path('admin', views.cargarAdmin),
    path('addProd',views.addProd),
    path('editProd',views.editProd),
    path('delProd/<sku>',views.delProd),
    path('sendPed/<idB>',views.sendPed),
    path('deliverPed/<idB>',views.deliverPed),
    path('loginForm',views.logIn),
    path('regForm',views.regForm),
    path('closeSession',views.closeSession),
    #api
    path('api/productos/', views.ProductoListAPIView.as_view(), name='producto-list'),#vista
    path('api/productos/create/', views.ProductoCreateAPIView.as_view(), name='producto-create'),#crear
    path('api/productos/<int:pk>/', views.ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto-detail'),#ver o modificar o eliminar o actualizar y colocar en el link el sku definido del producto
]