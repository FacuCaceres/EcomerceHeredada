from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('', views.sobrenosotros, name = 'sobrenosotros'),

]