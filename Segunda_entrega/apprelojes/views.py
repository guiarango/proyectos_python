from django.shortcuts import render
from apprelojes.models import Producto,Categoria,ComentariosPagina
from apprelojes.forms import ProductoFormulario,CategoriaFormulario,ComentarioFormulario

# Create your views here.

def vista_home(request):
    productos=Producto.objects.all()
    comentarios=ComentariosPagina.objects.all()
    contexto={"comentarios":comentarios,"diccionario_de_productos":productos[:4]}
    return render(request,"apprelojes/index.html",contexto)

def vista_categoria(request,id):
    resultados=Producto.objects.filter(categoria_id=id)
    resultados=list(resultados)
    contexto={"diccionario_de_productos":resultados}
    return render(request,"apprelojes/categoria.html",contexto)


def vista_crear_producto(request):
    if request.method=="POST":
        formulario=ProductoFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            data=formulario.cleaned_data
            producto=Producto(nombre=data["nombre"], precio=data["precio"], descuento=data["descuento"], descripcion=data["descripcion"], categoria_id=data["categoria_id"][0], url_nueva_imagen=data["url_nueva_imagen"])

            producto.save()

    formulario=ProductoFormulario()    
    contexto={"formulario":formulario}
    return render(request,"apprelojes/crear_producto.html",contexto)


def vista_crear_categoria(request):
    if request.method=="POST":
        formulario=CategoriaFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            producto=Categoria(nombre=data["nombre"])

            producto.save()

    formulario=CategoriaFormulario()    
    contexto={"formulario":formulario}
    return render(request,"apprelojes/crear_categoria.html",contexto)


def vista_crear_comentario(request):
    if request.method=="POST":
        formulario=ComentarioFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            producto=ComentariosPagina(nombre_usuario=data["nombre_usuario"],apellido_usuario=data["apellido_usuario"],comentario=data["comentario"])

            producto.save()

    formulario=ComentarioFormulario()    
    contexto={"formulario":formulario}
    return render(request,"apprelojes/crear_comentario.html",contexto)


def vista_buscar_producto(request):

    return render(request,"apprelojes/buscar_producto.html")

def vista_resultados_busqueda_productos(request):
    nombre_producto=request.GET["nombre_curso"]

    productos=Producto.objects.filter(nombre__icontains=nombre_producto)

    contexto={"diccionario_de_productos":list(productos)}

    return render(request,"apprelojes/resultados_busqueda_productos.html",contexto)