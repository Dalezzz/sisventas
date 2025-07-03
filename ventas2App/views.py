# Create your views here.
from django.shortcuts import render,redirect
from ventas2App.models import CabeceraVenta,DetalleVenta,Tipo,Parametro
from django.db.models import Q
from .forms import CabeceraVentaForm,DetalleVentaForm,DetalleVentaFormSet
#from .forms import CategoriaForm,UnidadesForm,ProductoForm
from django.http import JsonResponse
from seguridadApp.models import Cliente
from ventasApp.models import Productos

# Create your views here.
# Configurar
def listarventa(request):
    queryset = request.GET.get("buscar")
    if queryset:
        venta = CabeceraVenta.objects.filter(
            Q(descripcion__icontains=queryset),
            estado='1'
        ).distinct()
    else:
        venta = CabeceraVenta.objects.filter(estado='1')
    
    context = {'ventas': venta}
    return render(request, "ventas/index.html", context)

def agregarventa(request):
    if request.method == "POST":
        form_cabecera = CabeceraVentaForm(request.POST)

        if form_cabecera.is_valid():
            cabecera = form_cabecera.save()

            # Obtenemos listas de los datos de los detalles
            ids_producto = request.POST.getlist("cod_producto[]")
            precios = request.POST.getlist("pventa[]")
            cantidades = request.POST.getlist("cantidad[]")

            # Validación: ¿Hay al menos un detalle con cantidad >0?
            tiene_detalles = False
            for cantidad in cantidades:
                if cantidad.strip() and float(cantidad) > 0:
                    tiene_detalles = True
                    break

            if not tiene_detalles:
                # Borramos la cabecera si no hay detalles válidos
                cabecera.delete()
                form_cabecera.add_error(None, "Debe ingresar al menos un detalle con cantidad mayor a cero.")
            else:
                # Creamos cada detalle
                for i in range(len(ids_producto)):
                    if not cantidades[i].strip() or float(cantidades[i]) <= 0:
                        continue  # Saltar filas vacías o con cantidad 0

                    DetalleVenta.objects.create(
                        cabecera=cabecera,
                        idproducto_id=ids_producto[i],
                        precio=precios[i],
                        cantidad=cantidades[i]
                    )

                    # Descontar stock
                    producto = Productos.objects.get(pk=ids_producto[i])
                    producto.cantidad -= float(cantidades[i])
                    producto.save()

                return redirect("listarventas")

    else:
        form_cabecera = CabeceraVentaForm()

    productos = Productos.objects.all()
    context = {
        "form_cabecera": form_cabecera,
        "productos": productos
    }
    return render(request, "ventas/agregar.html", context)




#def editarventa(request,id):
#    categoria=Categoria.objects.get(id=id)
#    if request.method=="POST":
#        form=CategoriaForm(request.POST,instance=categoria)
#        if form.is_valid():
#            form.save() 
#            return redirect("listarcategoria") 
#    else:
#        form=CategoriaForm(instance=categoria)
#    context={"form":form} 
#    return render(request,"categoria/editar.html",context) 
    


def eliminarventa(request, id):
    venta = CabeceraVenta.objects.get(id=id)

    detalles = DetalleVenta.objects.filter(cabecera=venta)
    for detalle in detalles:
        producto = detalle.idproducto
        producto.cantidad += detalle.cantidad
        producto.save()

    # Borrar los detalles
    detalles.delete()

    # Marcar la venta como eliminada
    venta.estado = '0'
    venta.save()

    return redirect('listarventas')



def api_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        data = {
            'dniruc': cliente.dniruc,
            'direccion': cliente.direccion,
            # Otros campos si quieres
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

def api_tipo(request, tipo_id):
    try:
        tipo = Tipo.objects.get(pk=tipo_id)
        parametro = Parametro.objects.get(pk=tipo_id)
        nrodoc = f"{parametro.numeracion}"
        return JsonResponse({'nrodoc': nrodoc})
    except Tipo.DoesNotExist:
        return JsonResponse({'error': 'Tipo no encontrado'}, status=404)
    except Parametro.DoesNotExist:
        return JsonResponse({'error': 'No hay parámetro con id igual a tipo_id'}, status=404)

def api_producto(request, producto_id):
    try:
        producto = Productos.objects.get(pk=producto_id)
        data = {
            'stock': producto.cantidad,
            'precio': str(producto.precio),
            'unidad': producto.unidades.descripcion
        }
        return JsonResponse(data)
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)