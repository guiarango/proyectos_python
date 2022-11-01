from django.db import models
from django.forms import DateField

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    cumpleanos=models.DateField(null=True)