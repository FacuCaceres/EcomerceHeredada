from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from numpy import imag

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    # imagen = models.ImageField(upload_to='servicios')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return f'NOMBRE : {self.nombre} DESCRIPCION : {self.descripcion}'
