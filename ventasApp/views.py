from django.shortcuts import render,redirect
from ventasApp.models import Categoria,Unidades,Productos
from django.db.models import Q
from .forms import CategoriaForm,UnidadesForm,ProductoForm
# Create your views here.

def listarcategoria(request):
    queryset=request.GET.get("buscar")
    categoria=Categoria.objects.filter(estado=True) 
    if queryset:
        categoria=Categoria.objects.filter(
         Q(descripcion__icontains=queryset),estado=True
         ).distinct() 
    context={'categoria':categoria}
    return render(request,"categoria/index.html",context) 

def agregarcategoria(request):
    if request.method=="POST":
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("listarcategoria") 
    else:
        form=CategoriaForm()
    context={'form':form} 
    return render(request,"categoria/agregar.html",context) 


def editarcategoria(request,id):
    categoria=Categoria.objects.get(id=id)
    if request.method=="POST":
        form=CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save() 
            return redirect("listarcategoria") 
    else:
        form=CategoriaForm(instance=categoria)
    context={"form":form} 
    return render(request,"categoria/editar.html",context) 
    


def eliminarcategoria(request,id):
    categoria=Categoria.objects.get(id=id) 
    categoria.estado=False
    categoria.save()
    return redirect("listarcategoria") 
#Unidades

def listarunidades(request):
    query = request.GET.get("buscar")
    unidades = Unidades.objects.filter(estado=True)
    if query:
        unidades = Unidades.objects.filter(
            Q(descripcion__icontains=query), estado=True
        ).distinct()
    return render(request, "unidades/index.html", {'unidades': unidades})

def agregarunidades(request):
    if request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarunidades")
    else:
        form = UnidadesForm()
    return render(request, "unidades/agregar.html", {'form': form})

def editarunidades(request, id):
    unidad = Unidades.objects.get(id=id)
    if request.method == "POST":
        form = UnidadesForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect("listarunidades")
    else:
        form = UnidadesForm(instance=unidad)
    return render(request, "unidades/editar.html", {'form': form})

def eliminarunidades(request, id):
    unidad = Unidades.objects.get(id=id)
    unidad.estado = False
    unidad.save()
    return redirect("listarunidades")

#Productos

def listarproducto(request):
    queryset = request.GET.get("buscar")
    productos = Productos.objects.filter(estado=True)
    if queryset:
        productos = Productos.objects.filter(
            Q(descripcion__icontains=queryset), estado=True
        ).distinct()
    context = {'productos': productos}
    return render(request, "productos/index.html", context)

def agregarproducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarproducto")
    else:
        form = ProductoForm()
    context = {'form': form}
    return render(request, "productos/agregar.html", context)

def editarproducto(request, id):
    producto = Productos.objects.get(id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("listarproducto")
    else:
        form = ProductoForm(instance=producto)
    context = {"form": form}
    return render(request, "productos/editar.html", context)

def eliminarproducto(request, id):
    producto = Productos.objects.get(id=id)
    producto.estado = False
    producto.save()
    return redirect("listarproducto")