from django import forms 
from django.forms import fields, modelformset_factory
from .models import Tipo,CabeceraVenta,DetalleVenta
from ventasApp.models import Productos
from seguridadApp.models import Cliente


class CabeceraVentaForm(forms.ModelForm):

    class Meta:
        model= CabeceraVenta
        fields= ['idcliente', 'fechaventa', 'idtipo', 'estado', 'total', 'nrodoc', 'subtotal', 'igv']
        widgets = {
            'fechaventa': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'nrodoc': forms.TextInput(attrs={'readonly': 'readonly'}),
            'subtotal': forms.TextInput(attrs={'readonly': 'readonly'}),
            'igv': forms.TextInput(attrs={'readonly': 'readonly'}),
            'total': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CabeceraVentaForm, self).__init__(*args, **kwargs)
        self.fields['idcliente'].queryset = Cliente.objects.all()
        self.fields['idtipo'].queryset = Tipo.objects.all()
        self.fields['estado'].initial = "1"



class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['idproducto', 'precio', 'cantidad']
        

    def __init__(self, *args, **kwargs):
        super(DetalleVentaForm, self).__init__(*args, **kwargs)
        self.fields['idproducto'].queryset = Productos.objects.all()

DetalleVentaFormSet = modelformset_factory(
    DetalleVenta,
    form=DetalleVentaForm,
    extra=10,  # Puedes poner más si quieres permitir más filas
    can_delete=True  # Opcional, si quieres permitir eliminar detalles
)

#class VentaForm(forms.ModelForm):
#    class Meta: