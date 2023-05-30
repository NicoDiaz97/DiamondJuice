from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from AppTienda.models import Producto, Pedido, ArticulosPedido
from AppTienda.forms import PedidoForm, ArticulosForm, ArticulosPedidoFormSet

def galeria_productos(request):
    contexto = {
        'productos': Producto.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='AppTienda/galeria_productos.html',
        context=contexto,
    )
    return http_response

class visualizarProductoDetailView(DetailView):
    model       = Producto
    success_url = reverse_lazy('galeria_productos')

class visualizar_pedidosListView(LoginRequiredMixin, ListView):
    # model           = Pedido
    # queryset        = Pedido.objects.filter(user__exact=)
    template_name   = 'AppTienda/pedidos.html'
    def get_queryset(self) -> QuerySet[Any]:
        return Pedido.objects.filter(user=self.request.user)

@login_required
def pedido_detail(request, pedido_id):
    # Obtener el pedido por su id o devolver un error 404 si no existe
    pedido = get_object_or_404(Pedido, id=pedido_id)
    # Obtener los articulos asociados al pedido
    articulos = pedido.articulospedido_set.all()
    # Renderizar el template con el pedido y los articulos como contexto
    return render(request, "AppTienda/pedido_detail.html", {"pedido": pedido, "articulos": articulos})

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        articulos_formset = ArticulosPedidoFormSet(request.POST)
        if pedido_form.is_valid() and articulos_formset.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            for articulo_form in articulos_formset:
                articulo = articulo_form.save(commit=False)
                articulo.pedido_id = pedido
                articulo.save()
            return redirect('ver-pedido', pedido.id)
    else:
        pedido_form = PedidoForm()
        articulos_formset = ArticulosPedidoFormSet(queryset=ArticulosPedido.objects.none())
        context = {"pedido_form": pedido_form, "articulos_formset": articulos_formset}
        return render(request, 'AppTienda/crearpedido.html', context)
