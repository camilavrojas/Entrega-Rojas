from django.urls import path
from .views import inicio, mi_template, publicaciones

urlpatterns = [
    path('', inicio, name='inicio'),
    path('template/', mi_template, name='mi_template'),
    path('publicaciones/', publicaciones, name='publicaciones')
]