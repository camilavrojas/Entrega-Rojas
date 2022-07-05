from django.shortcuts import redirect, render
from blog.forms import BuscarPublicacion, FormPublicacion
from .models import Publicacion
from datetime import datetime
# from django.template import loader
# from django.http import HttpResponse

def inicio(request):
    return render(request, 'index.html')


def crear_publicacion(request):
    if request.method == 'POST':
        form = FormPublicacion(request.POST)

        if form.is_valid(): 
            data = form.cleaned_data
            fecha = data.get('fecha_creacion')

            publicacion = Publicacion(
                titulo=data.get('titulo'), 
                contenido=data.get('contenido'), 
                fecha_creacion=fecha if fecha else datetime.now())
            publicacion.save()

            # lista_publicacion = Publicacion.objects.all()
            # form = BuscarPublicacion()
            # return render(request, 'publicacion.html', {'lista_publicacion':lista_publicacion, 'form':form})
            return redirect('publicaciones')
        else: 
            return render(request, 'formulario.html', {'form':form})

    form_publicacion = FormPublicacion()
    return render(request, 'formulario.html', {'form':form_publicacion})


def publicaciones(request): 
    titulo_de_busqueda = request.GET.get('titulo')
    
    if titulo_de_busqueda:
        publicaciones = Publicacion.objects.filter(titulo__icontains=titulo_de_busqueda) 
    else: 
        publicaciones = Publicacion.objects.all()

    form = BuscarPublicacion()
    return render(request, 'publicacion.html', {'publicaciones':publicaciones, 'form':form})


