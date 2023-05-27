from django import forms
from betterforms.multiform import MultiModelForm

from AppTienda.models import Pedido, ArticulosPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model   = Pedido
        fields  = ['tipo_retiro', 'direccion_envio', 'comentarios_adicionales']

class ArticulosForm(forms.ModelForm):
    class Meta:
        model   = ArticulosPedido
        fields  = ['usuario_pedido_id', 'pedido_id', 'producto', 'cantidad']
