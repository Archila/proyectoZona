from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Tipo
from .models import Proveedor
from .models import Producto
from .models import Actividad
from .models import Cotizacion
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render(request, 'constructora/home.html')

#CRUDO PRODUCTO
def lista_productos(request):
    prods = Producto.objects.filter()
    return render(request, 'constructora/productos.html',{'prod': prods})

def editar_producto(request,pk):
    p = get_object_or_404(Producto,pk= pk)
    proveedores = Proveedor.objects.all()
    tipos = Tipo.objects.all()
    return render(request,'constructora/editar_producto.html',{'p':p, 'prov':proveedores, 'tipos':tipos})

def nuevo_producto(request):
    proveedores = Proveedor.objects.all()
    tipos = Tipo.objects.all()
    return render(request, 'constructora/nuevo_producto.html',{'prov':proveedores, 'tipos':tipos})

def insertar_producto(request):
    provee = get_object_or_404(Proveedor, pk= request.POST['proveedor'])
    tipo = get_object_or_404(Tipo, pk= request.POST['tipo'])
    producto = Producto(nombre=request.POST['nombre'],unidad=request.POST['unidad'],precio=request.POST['precio'],marca="--", tipo=tipo,proveedor=provee)
    producto.save()
    prods = Producto.objects.all()
    return render(request, 'constructora/productos.html',{'prod': prods})

def eliminar_producto(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    prods = Producto.objects.all()
    return render(request, 'constructora/productos.html',{'prod': prods})

def actualizar_producto(request,pk):
    try:
        producto = get_object_or_404(Producto, pk=pk)
        producto.nombre = request.POST['nombre']
        producto.unidad = request.POST['unidad']
        producto.precio = request.POST['precio']
        provee = get_object_or_404(Proveedor,pk= request.POST['proveedor'])
        tipo = get_object_or_404(Tipo,pk= request.POST['tipo'])
        producto.proveedor = provee
        producto.tipo=tipo
        producto.save()


    except Exception as e:
        raise
    prods = Producto.objects.filter()
    return render(request, 'constructora/productos.html',{'prod': prods})

def prueba(request):
    formulario = ProductoForm(request.POST)
    return render(request,'constructora/prueba.html',{'formulario':formulario})

#CRUD PROVEEDOR
def lista_proveedores(request):
    provs = Proveedor.objects.all()
    return render(request, 'constructora/proveedores.html',{'prov': provs})

def editar_proveedor(request,pk):
    p = get_object_or_404(Proveedor,pk= pk)
    return render(request,'constructora/editar_proveedor.html',{'p':p})

def nuevo_proveedor(request):
    return render(request, 'constructora/nuevo_proveedor.html')

def insertar_proveedor(request):
    prov = Proveedor(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'])
    prov.save()
    provs = Proveedor.objects.all()
    return render(request, 'constructora/proveedores.html',{'prov': provs})

def eliminar_proveedor(request,pk):
    prov = get_object_or_404(Proveedor, pk=pk)
    prov.delete()
    provs = Proveedor.objects.all()
    return render(request, 'constructora/proveedores.html',{'prov': provs})

def actualizar_proveedor(request,pk):
    try:
        prov = get_object_or_404(Proveedor, pk=pk)
        prov.nombre = request.POST['nombre']
        prov.descripcion = request.POST['descripcion']
        prov.save()
    except Exception as e:
        raise
    provs = Proveedor.objects.all()
    return render(request, 'constructora/proveedores.html',{'prov': provs})


#CRUD PROYECTO
def nuevo_proyecto(request):
    return render(request,'constructora/home.html')
