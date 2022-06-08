from tkinter import N
from django.shortcuts import render
from sobrenosotros.models import Nosotros
# Create your views here.
def sobrenosotros(request):
    nosotros = Nosotros.objects.all()
    context = {
        'sobrenosotros' : nosotros
    }
    return render(request,'sobrenosotros/sobrenosotros.html',context)