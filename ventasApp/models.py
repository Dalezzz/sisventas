from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Unidades(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Productos(models.Model):
    descripcion = models.CharField(max_length=40)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    unidades = models.ForeignKey(Unidades, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

