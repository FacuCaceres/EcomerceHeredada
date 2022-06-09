from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [

    path('', views.productos, name = 'productos'),
    path('buscar/',views.buscar_productos , name = 'buscar_productos'),
    path('detalle-producto/<int:id>/',views.detalle_producto , name = 'detalle-producto'),
    path('eliminar-producto/<int:id>/',views.eliminar_producto , name = 'eliminar-producto'),
    path('update_product/<int:pk>/',views.Update_product.as_view() , name = 'update_product'),
]