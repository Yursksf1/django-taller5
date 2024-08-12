from django.shortcuts import render
from myapp.models import Producto, Categoria

# Create your views here.

def list_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias
    }
    return render(request, 'myapp/list-categorias.html', context)

def list_productos(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'myapp/list-productos.html', context)

def detail_productos(request, id):
    producto = Producto.objects.filter(code=id).first()
    context = {
        "producto": producto
    }
    return render(request, 'myapp/detail-productos.html', context)

def index(request):
    context = {
        
    }
    return render(request, 'myapp/index.html', context)