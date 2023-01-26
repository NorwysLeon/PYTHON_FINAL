from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
    #path('perfil/', perfil, name="perfil"),
    
]