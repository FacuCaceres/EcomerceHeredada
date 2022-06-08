from django.shortcuts import render
from servicios.models import Servicios

# Create your views here.
def servicios(request):
    servicio = Servicios.objects.all()
    context = {
        'servicio' : servicio
    }
    
    return render(request,'servicios/servicios.html',context)