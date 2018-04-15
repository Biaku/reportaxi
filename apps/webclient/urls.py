from django.contrib import admin
from django.urls import path

from apps.webclient import views

app_name = 'webclient'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('taxis/buscar/', views.SeriviciosList.as_view(), name='servicio-busqueda'),
    path('taxis/', views.SeriviciosList.as_view(), name='servicios'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('publicar/', views.publicar, name='publicar'),
    path('tarifas/', views.tarifas, name='tarifas'),
    path('sectores/', views.sectores, name='sectores'),
    path('sabias-que/', views.sabias_que, name='sabias_que'),

    path('email/', views.enviar_email),
]
