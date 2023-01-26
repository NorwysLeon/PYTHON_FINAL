from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required  #para vistas basadas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en class
from django.contrib.auth.models import User


def registro(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "Appblog/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "Appregistro/registro.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "Appregistro/registro.html", {"form": form, "mensaje":"Error al crear el usuario"})



