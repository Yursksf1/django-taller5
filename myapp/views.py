from datetime import datetime, timedelta
from django.shortcuts import render
from myapp.models import Producto, Categoria
from myapp.forms import ProductoForm

# Create your views here.

def list_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias
    }
    return render(request, 'myapp/list-categorias.html', context)

def detail_categoria(request, id):
    categoria = Categoria.objects.filter(id=id).first()
    productos = Producto.objects.filter(categoria_id=id).all()

    context = {
        "categoria": categoria,
        "productos": productos
    }
    return render(request, 'myapp/detail-categoria.html', context)


def list_productos(request):
    productos = []
    context = {}
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

def add_productos(request):
    form = ProductoForm()
    context = {
        "form": form
    }
    method = request.method
    if method == 'POST':
        # todo: revisar esto 
        data = request.POST
        code = data.get('code')
        name = data.get('name')
        brand = data.get('brand')
        reference = data.get('reference')
        description = data.get('description')
        price = data.get('price')
        batch = data.get('batch')
        manufacturing = data.get('manufacturing')
        expedition = data.get('expedition')
        categoria_id = data.get('categoria')

        producto = Producto(
            code=code,
            name=name,
            brand=brand,
            reference=reference,
            description=description,
            price=price,
            batch=batch,
        )
        producto.save()

    return render(request, 'myapp/add-producto.html', context)

def dashboard(request):

    today = datetime.now().today().date()
    fecha_futura = today + timedelta(days=60) # agregamos 2 meses

    productos_por_vencer = Producto.objects.filter(expedition__lt=fecha_futura).count()

    context = {
        'productos_por_vencer': productos_por_vencer,
    }
    return render(request, 'myapp/dashboard.html', context)


def prodcuts_por_vencer(request):
    today = datetime.now().today().date()
    fecha_futura = today + timedelta(days=60) # agregamos 2 meses

    productos = []
    context = {}
    product_query = Producto.objects
    product_query = product_query.filter(expedition__lt=fecha_futura)

    filtro = request.GET.get('search')
    if filtro:
        product_query = product_query.filter(name__icontains=filtro)

    productos = product_query.all()

    context = {
        "productos": productos,
        "today": today
    }
    return render(request, 'myapp/list-productos.html', context)
