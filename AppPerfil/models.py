from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


    
class Perfil(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    nombre=models.CharField(max_length=100)
    web=models.URLField()
    email=models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion=RichTextField(blank=True, null=True)
    password1=models.CharField(max_length=8)
    password2=models.CharField(max_length=8)
   

    def __str__(self):
        return f"{self.imagen} - {self.nombre} - {self.descripcion} - {self.web} - {self.email}"


class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.imagen} - {self.user}"