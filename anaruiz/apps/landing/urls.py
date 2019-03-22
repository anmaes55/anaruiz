from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mensaje-enviado', views.mensaje_enviado, name='mensaje-enviado'),
]
