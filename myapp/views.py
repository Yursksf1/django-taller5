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
    productos = []
    filtro = request.GET.get('search')
    if filtro:
        productos = Producto.objects.filter(name__icontains=filtro).all()
    else:
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

def delete_productos(request, id):
    producto = Producto.objects.filter(code=id).first()
    producto.delete()

    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'myapp/list-productos.html', context)

def update_productos(request, id):
    producto = Producto.objects.filter(code=id).first()
    method = request.method
    if method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        producto.name = name
        producto.description = description
        producto.save()

    context = {
        "producto": producto
    }
    return render(request, 'myapp/update-productos.html', context)

def index(request):
    context = {
        
    }
    return render(request, 'myapp/index.html', context)

def dashboard(request):
    context = {
        
    }
    return render(request, 'myapp/dashboard.html', context)