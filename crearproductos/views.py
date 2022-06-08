from django.http import HttpResponse
from django.shortcuts import render
from  crearproductos.forms import Form_Productos
from productos.models import Products

# Create your views here.
def crearproductos(request):
    method_get = request.method == 'GET' 
    if method_get:
        formulario = Form_Productos()
        context = {
            'form': formulario
        }
        return render(request,'crearproductos/crearproductos.html',context=context)
    else:
        print('COSAS DE POST',request.POST)
        form = Form_Productos(request.POST)
        if form.is_valid():
            nuevo_producto = Products.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                descripcion = form.cleaned_data['descripcion'],
                cod = form.cleaned_data['cod'],
                is_active = form.cleaned_data['is_active'],
            )
            context = {
                'n_producto':nuevo_producto
            }
            return render(request,'crearproductos/crearproductos.html',context=context)