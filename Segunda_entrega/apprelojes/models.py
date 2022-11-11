from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=20)

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    descuento=models.IntegerField()
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    url_nueva_imagen=models.ImageField(null=True, blank=True,upload_to="product/")

class ComentariosPagina(models.Model):
    nombre_usuario=models.CharField(max_length=50)
    apellido_usuario=models.CharField(max_length=60)
    comentario=models.TextField()