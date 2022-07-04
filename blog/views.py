from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader
# from .models import Publicacion

def inicio(request):
    return render(request, 'index.html')
    
def mi_template(request):

    # template = loader.get_template('mi_template.html')
    # render = template.render({})
    # return HttpResponse(render)

    return render(request, 'mi_template.html', {})