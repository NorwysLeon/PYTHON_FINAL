from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('login/', login_usuario, name="login"), #No se puede llamar solo login porque ya existe una funcion login por eso login_request, puede tener cualquier nombre.
    path('logout/', LogoutView.as_view() , name="logout"),
    path('acceso/', acceso, name="acceso"),

        
]