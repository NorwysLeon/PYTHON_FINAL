from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RegistroUsuarioForm(UserCreationForm): #Estos son los campos del admin usuario, username esta por deecto
    email= forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
  
    class Meta: #configura el formulario
        model=User
        fields= ["username", "email", "password1", "password2"] #Camposque muestra el formulario
        help_texts= {k:"" for k in fields} #Asigna un valor vacio a cada texto de ayuda del formulario.



