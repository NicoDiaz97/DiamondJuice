from django.contrib import admin
from django.urls import path
from AppTienda.views import galeria_productos, visualizarProductoDetailView, crearPedido

urlpatterns = [
    path('productos/', galeria_productos, name='galeria-productos'),
    path('ver-producto/<int:pk>/', visualizarProductoDetailView.as_view(), name='ver-producto'),
    path('crear-pedido/', crearPedido, name='crear-pedido'),

]