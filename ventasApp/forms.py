from django import forms 
from django.forms import fields 
from.models import Categoria, Unidades, Productos


class CategoriaForm(forms.ModelForm):

    class Meta:
        model=Categoria
        fields=['descripcion','estado'] 

class UnidadesForm(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = ['descripcion', 'estado']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['descripcion', 'categorias', 'precio', 'cantidad', 'unidades', 'estado']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['categorias'].queryset = Categoria.objects.filter(estado=True)
        self.fields['unidades'].queryset = Unidades.objects.filter(estado=True)