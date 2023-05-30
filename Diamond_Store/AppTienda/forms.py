from django import forms
from django.forms import modelformset_factory

from AppTienda.models import Pedido, Producto, ArticulosPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model   = Pedido
        fields  = ['tipo_retiro', 'direccion_envio', 'comentarios_adicionales']

class ArticulosForm(forms.Form):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())


ArticulosPedidoFormSet = modelformset_factory(
    ArticulosPedido, fields=["producto", "cantidad"]
    )