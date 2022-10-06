from django.urls import path
from juegosApp import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('nosotros', views.nosotros, name="Nosotros"),
    path('juegos', views.juegos, name="Juegos"), 
]