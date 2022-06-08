from pyexpat import model
from django.contrib import admin
from servicios.models import Servicios
# Register your models here.

# class ServicioAdmin(admin.ModelAdmin):
#     readonly_fields = ('created','updated')

admin.site.register(Servicios)