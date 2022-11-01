# import os
from django.shortcuts import render
from django.template import loader
from familiares.models import Familiar 
from django.http import HttpResponse
# from MVTGuilleroArango.settings import BASE_DIR 

# Create your views here.
def vista_familiares(request):
    listado_familiares=Familiar.objects.all()
    datos={"familiares":listado_familiares}
    plantilla=loader.get_template("plantilla_familia.html")
    documento=plantilla.render(datos)
    return HttpResponse(documento)
