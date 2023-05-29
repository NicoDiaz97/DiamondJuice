from django.contrib import admin
from AppTienda.models import Producto, Pedido, ArticulosPedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ArticulosPedido)