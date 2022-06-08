from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('', views.productos, name = 'productos'),
    path('buscar/',views.buscar_productos , name = 'buscar_productos'),
]