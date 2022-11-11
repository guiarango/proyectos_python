from django import forms
from apprelojes.models import Categoria

datosCategoria=Categoria.objects.all()
datosListaCategoria=[]
for categoria in datosCategoria:
    datosListaCategoria.append((categoria.id,categoria.nombre))

class ProductoFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.FloatField()
    descuento=forms.CharField()
    descripcion=forms.CharField()
    categoria_id=forms.MultipleChoiceField(required=False,
        choices=datosListaCategoria)
    url_nueva_imagen=forms.ImageField()

class CategoriaFormulario(forms.Form):
    nombre=forms.CharField()

class ComentarioFormulario(forms.Form):
    nombre_usuario=forms.CharField()
    apellido_usuario=forms.CharField()
    comentario=forms.CharField()