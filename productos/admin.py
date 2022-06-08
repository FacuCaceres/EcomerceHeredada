from django.contrib import admin
from productos.models import Products
# Register your models here.

# REGISTRO NORMAL PARA METODOS __STR__
# admin.site.register(Products)



# REGISTRO CON CLASES DECORADORAS   "ES RECOMENDABLE USAR ESTE METODO"
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','is_active']