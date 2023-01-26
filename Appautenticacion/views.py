from django.shortcuts import render
from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required  #para vistas basadas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en class
from django.contrib.auth.models import User

# Create your views here.




def login_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            contraseña=info["password"]
            usuario=authenticate(username=usu, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render (request, "Appblog/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamemte"})
            else:
                return render(request, "Appautenticacion/login.html", {"form": form, "mensaje": "Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "Appautenticacion/login.html", {"form": form, "mensaje": "Usuario  y/o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render (request,"Appautenticacion/login.html", {"form": form})




def acceso(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "Appblog/inicio.html", {"mensaje": f"Usuario {username} fue creado exitosamente.!"})      
        else:
            return render(request, "Apprautenticacion/acceso.html", {"form": form, "mensaje": "ERROR AL CREAR USUARIO!"})  
    else:
        form=RegistroUsuarioForm()
        return render(request, "Apprautenticacion/acceso.html", {"form":form})
