from django.contrib import admin
from .models import Categoria, Unidades, Productos


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Unidades)
admin.site.register(Productos)
