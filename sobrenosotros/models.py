from tabnanny import verbose
from django.db import models

# Create your models here.

class Nosotros(models.Model):
    descripcion = models.CharField(max_length=1000)
    mision = models.CharField(max_length=1000)
    vision = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Nosotro'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return f'SOBRE NOSOTROS'