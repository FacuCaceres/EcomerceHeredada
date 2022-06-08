from tabnanny import verbose
from django.db import models

# Create your models here.
class Products(models.Model):
     nombre = models.CharField(max_length=50)
     precio = models.FloatField()
     descripcion = models.CharField(max_length=200)
     cod = models.CharField(max_length=30, unique=True)
     is_active = models.BooleanField(default=True)
     class Meta:
         verbose_name = 'producto'
         verbose_name_plural = 'productos'

    # METODO DE PRESENTACION DE CLASES __STR__   
    #  def __str__(self):
    #       return f'{self.nombre} {self.precio} {self.descripcion} {self.is_active}'
        
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return f'{self.nombre} {self.descripcion}'