from django.db import models

from seguridadApp.models import Cliente
from ventasApp.models import Productos
from django.utils import timezone


# Create your models here.
class Tipo(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion
    
class Parametro(models.Model):
    numeracion = models.CharField(max_length=15)
    serie = models.CharField(max_length=3)

    #def __str__(self):
    #    return self.descripcion
    
#Configurar/hecho
class CabeceraVenta(models.Model):
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaventa = models.DateField(default=timezone.now)
    idtipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=11)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    nrodoc = models.CharField(max_length=12)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2)
    igv = models.DecimalField(max_digits=20, decimal_places=2)

class DetalleVenta(models.Model):
    cabecera = models.ForeignKey(CabeceraVenta, on_delete=models.CASCADE)
    idproducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad = models.IntegerField()
