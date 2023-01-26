from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField



    



"""class UserEditForm(UserCreationForm): 
    email= forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")
  
    class Meta: #configura el formulario
        model=User
        fields= ["email", "password1", "password2", "first_name", "last_name"] #Camposque muestra el formulario
        help_texts= {k:"" for k in fields} #Asigna un valor vacio a cada texto de ayuda del formulario."""


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class PerfilForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    nombre=forms.CharField(label="nombre")
    descripcion=RichTextField(blank=True, null=True)
    web=forms.URLField(label="web")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    
    
