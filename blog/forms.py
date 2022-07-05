from django import forms

class FormPublicacion(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=300)
    fecha_creacion = forms.DateField(required=False)

class BuscarPublicacion(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
