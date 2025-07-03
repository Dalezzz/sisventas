from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if usuario:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required(login_url='login')
def homePage(request):
    return render(request, "bienvenido.html")

def salir(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("login")

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar.html'
    context_object_name = 'clientes'
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombres', 'apellidos', 'dniruc', 'correo', 'telefono', 'direccion']
    template_name = 'cliente/formulario.html'
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombres', 'apellidos', 'dniruc', 'correo', 'telefono', 'direccion']
    template_name = 'cliente/formulario.html'
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('clientes')