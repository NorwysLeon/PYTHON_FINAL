from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from Appblog.form import *

from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required  #para vistas basadas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en class
from django.contrib.auth.models import User


def inicio(request):
    return render(request, "inicio.html")

def acercademi(request):
    return render (request, "acercademi.html")

def blogFormulario(request):
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data #me trae el input de html y lo convierte en diccionario
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            fecha= informacion["fecha"]
            #cuerpo
            imagen= informacion["imagen"]
            blog= Blog(titulo=titulo, subtitulo=subtitulo, fecha=fecha, imagen=imagen)
            blog.autor=request.user 
            blog.save()
            blogs=Blog.objects.all()
            return render(request, "leerBlogs.html", {"blogs":blogs, "mensaje": "Post guardado correctamente"}) 
        else:
            return render(request, "blogFormulario.html", {"form":form, "mensaje": "Información no valida"})      
    else:
        formulario=BlogForm()
        return render(request, "blogFormulario.html", {"form": formulario, "mensaje": "Información no valida"})



def busquedaTitulo(request):
    return render(request, "busquedaTitulo.html")


def buscar(request):
    titulo=request.GET["titulo"]
    if titulo!="":
        blogs=Blog.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosBusqueda.html", {"blogs":blogs})
    else:
        return render (request, "busquedaTitulo.html", {"mensaje": "Favor ingresar un titulo para buscar"})


def leerBlogs(request):
    blogs=Blog.objects.all()
    return render (request, "leerBlogs.html", {"blogs":blogs})


def eliminarBlog(request, id):
    blog= Blog.objects.get(id=id) #Trae los datos del model Blog que concuerda con el id. como es get es uno solo.
    blog.delete()
    blogs=Blog.objects.all()
    return render(request, "leerBlogs.html", {"blogs":blogs, "mensaje": "Blog eliminado correctamente"})


def editarBlog(request, id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        form= BlogForm(request.POST, request.FILES)
        if form.is_valid():         #Verifica si el formulario es valido
            info=form.cleaned_data  #transforma del formulario al diccionario
            blog.titulo=info["titulo"]
            blog.subtitulo=info["subtitulo"]
            #blog.cuerpo=info["cuerpo"]
            blog.fecha=info["fecha"]
            blog.imagen=info["imagen"]
            blog.autor=request.user 
            blog.save()
            blogs=Blog.objects.all()
            return render (request, "leerBlogs.html", {"blogs": blogs, "mensaje": "Blog editado correctamente!"})
        pass
    else:
        formulario= BlogForm(initial= {"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "fecha":blog.fecha, "imagen":blog.imagen})  #Trae los datos iniciales del Blog
        return render (request, "editarBlog.html", {"form": formulario, "blog": blog})


#Permite listar todos los blogs de la BD, con información mínima de dicho blog.
class BlogList(LoginRequiredMixin, ListView):
    model=Blog
    template_name= "blogs.html"
