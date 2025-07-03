from django.urls import path,include 
from ventasApp.views import (
    listarcategoria, agregarcategoria, editarcategoria, eliminarcategoria
    ,listarunidades, agregarunidades, editarunidades, eliminarunidades
    ,listarproducto, agregarproducto, editarproducto, eliminarproducto
 )
from django.contrib.auth import views
urlpatterns = [ 
    path('listacategoria/',listarcategoria,name="listarcategoria"),
    path('agregarcategoria/',agregarcategoria,name="agregarcategoria"),
    path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"), 
    path('eliminarcategoria/<int:id>/',eliminarcategoria,name="eliminarcategoria"), 
    # Unidades
    path('listarunidades/', listarunidades, name="listarunidades"),
    path('agregarunidades/', agregarunidades, name="agregarunidades"),
    path('editarunidades/<int:id>/', editarunidades, name="editarunidades"),
    path('eliminarunidades/<int:id>/', eliminarunidades, name="eliminarunidades"),
    # Producto
    path('listarproducto/', listarproducto, name="listarproducto"),
    path('agregarproducto/', agregarproducto, name="agregarproducto"),
    path('editarproducto/<int:id>/', editarproducto, name="editarproducto"),
    path('eliminarproducto/<int:id>/', eliminarproducto, name="eliminarproducto"),
    ] 