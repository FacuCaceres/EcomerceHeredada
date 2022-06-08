from dataclasses import field
from django import forms
# from productos.models import Products

class Form_Productos(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()
    descripcion = forms.CharField(max_length=200)
    cod = forms.CharField(max_length=30)
    is_active = forms.BooleanField()




# MODELO MAS MODERNO Y CON LA MISMA FUNCIONALIDAD DEL DE ARRIBA 
# class Product_Form(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = '__all__' 