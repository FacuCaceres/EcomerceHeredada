from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from productos.models import Products
# Create your views here.
def productos(request):
    productos = Products.objects.all()
    context = { 'productos':productos  }
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

    

def detalle_producto(request, id):

    '''EL TRY EXCEPT ES UNA VENTAJA Y DESVENTAJA PORQUE EVITA QUE TU PROGRAMA SE ROMPA PERO A LA VEZ EVITA QUE 
    TU PROGRAMA TE AVISE CUAL ES EL ERROR EN CASO DE ROMPERSE ME PASO AHORA CON UN ERROR EN EL HTML
    ESTABA COMENTANDO UN CODIGO Y NO DEBI COMENTAR DEBI QUITARLO ES DECIR BORRARLO'''

    try:
        producto = Products.objects.get(id=id)
        context = {'detalle_prd':producto }
        return render(request,'productos/detalle-producto.html',context=context)
    except:
        return HttpResponse('PRODUCTO NO HALLADO')

def eliminar_producto(request,id):
    try:
        prd_a_eliminar = Products.objects.get(id=id)
        print(prd_a_eliminar.nombre)
        print(prd_a_eliminar.id)
        prd_a_eliminar.delete()
        context = {
            'message' : 'PRODUCTO ELIMINADO CORRECTAMENTE'
        }
        return render(request,'productos/productos.html',context=context)
    except:
        return HttpResponse('EL PRODUCTO NO SE PUDO ELIMINAR')



        