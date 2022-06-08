from multiprocessing import context
from django.shortcuts import render
from productos.models import Products
# Create your views here.
def productos(request):
    productos = Products.objects.all()
    context = {
        'productos':productos
    }
    return render(request,'productos/productos.html',context=context)

def buscar_productos(request):
    '''
    GET trae un solo producto se usa para buscar productos por ID o cuando tenemos bien definido que producto
    queremos buscar. Cuando deseamos buscar varios productos usamos FILTER por ejemplo si en una BD buscamos
    Coca Cola con FILTER nos traera todas las Coca Cola de todos los tamaños. 
    '''
    # productos = Products.objects.get(buscando)   
    
    productos = Products.objects.filter(nombre__icontains = request.GET['search'])
    context = {
        'prd_buscados' : productos
    }
    return render(request, 'productos/buscarproductos.html',context=context)