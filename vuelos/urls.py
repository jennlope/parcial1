from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro_vuelo, name='registro_vuelo'),
    path('lista/', views.lista_vuelos, name='lista_vuelos'),
    path('estadistica/', views.vuelo_estadisticas, name='vuelo_estadisticas'),
]