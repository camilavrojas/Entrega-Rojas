from django.urls import path
from .views import inicio, crear_publicacion, publicaciones, acerca

urlpatterns = [
    path('', inicio, name='inicio'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('formulario/', crear_publicacion, name='formulario'),
    path('acerca/', acerca, name='acerca') 
]