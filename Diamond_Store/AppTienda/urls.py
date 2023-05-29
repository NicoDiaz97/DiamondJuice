from django.contrib import admin
from django.urls import path
from AppTienda.views import galeria_productos, visualizarProductoDetailView, crearPedido, agregarArticulosPedido, insert_articulos, pedido_detail, create_order

urlpatterns = [
    path('productos/', galeria_productos, name='galeria-productos'),
    path('ver-producto/<int:pk>/', visualizarProductoDetailView.as_view(), name='ver-producto'),
    path('crear-pedido/', create_order, name='crear-pedido'),
    path('agregar-articulos/<int:pedido_id>/', insert_articulos, name='agregar-articulos'),
    path('ver-pedido/<int:pedido_id>/', pedido_detail, name='ver-pedido'),

]