from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from .forms import *

from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required  #para vistas basadas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en class
from django.contrib.auth.models import User




def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "Appblog/inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "AppPerfil/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppPErfil/agregarAvatar.html", {"form": form, "usuario": request.user})