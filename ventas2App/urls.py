from django.urls import path,include 
from ventas2App.views import ( 
    listarventa, agregarventa,eliminarventa,api_cliente, api_tipo,api_producto
 )
from django.contrib.auth import views
urlpatterns = [ 
    path('listaventas/',listarventa,name="listarventas"),
    path('agregarventa/',agregarventa,name="agregarventas"),
    path('eliminarventa/<int:id>/',eliminarventa,name="eliminarventa"), 
    path('api/cliente/<int:cliente_id>/', api_cliente, name='api_cliente'),
    path('api/tipo/<int:tipo_id>/', api_tipo, name='api_tipo'),
    path('api/producto/<int:producto_id>/', api_producto, name='api_producto'),
    ] 