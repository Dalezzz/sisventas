from django.urls import path
from .views import acceder, homePage, salir
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
)

urlpatterns = [
    path('', acceder, name='login'),
    path('home/', homePage, name='home'),
    path('logout/', salir, name='logout'),
    path('clientes/', ClienteListView.as_view(), name='clientes'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_nuevo'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
]