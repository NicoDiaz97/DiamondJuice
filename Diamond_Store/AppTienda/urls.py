from django.contrib import admin
from django.urls import path
from AppTienda.views import galeria_productos, visualizarProductoDetailView, pedido_detail, crear_pedido, visualizar_pedidosListView, eliminar_pedidoDeleteView

urlpatterns = [
    path('productos/', galeria_productos, name='galeria-productos'),
    path('ver-producto/<int:pk>/', visualizarProductoDetailView.as_view(), name='ver-producto'),
    path('pedidos/', visualizar_pedidosListView.as_view(), name='pedidos'),
    path('crear-pedido/', crear_pedido, name='crear-pedido'),
    path('ver-pedido/<int:pedido_id>/', pedido_detail, name='ver-pedido'),
    path('eliminar-pedido/<int:pk>/', eliminar_pedidoDeleteView.as_view(), name='eliminar-pedido'),

]