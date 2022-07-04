from django.urls import path
from .views import inicio, mi_template

urlpatterns = [
    path('', inicio),
    path('template/', mi_template)
]