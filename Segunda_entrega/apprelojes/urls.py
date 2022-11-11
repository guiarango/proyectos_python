from django.urls import path,include
from apprelojes.views import *

urlpatterns = [
    path('',vista_home,name="home"),
    path('categoria/<str:id>/',vista_categoria,name="categoria"),
    path('crear_producto/',vista_crear_producto,name="crear_producto"),
    path('crear_categoria/',vista_crear_categoria,name="crear_categoria"),
    path('crear_comentario/',vista_crear_comentario,name="crear_comentario"),
    path('buscar_producto/',vista_buscar_producto,name="buscar_producto"),
    path('buscar_producto/resultado/',vista_resultados_busqueda_productos,name="resultados_busqueda_productos")
]