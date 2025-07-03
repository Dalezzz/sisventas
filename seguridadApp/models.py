from django.db import models



class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dniruc = models.CharField(max_length=11, unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=9, blank=True)
    direccion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
