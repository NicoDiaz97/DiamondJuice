from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from AppTienda.models import Producto
from AppTienda.forms import PedidoForm, ArticulosForm

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

@login_required
def crearPedido(request):
    if request.method == 'POST':
        form    = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            return redirect('galeria-productos')
        else:
            print(form.errors)
    else:
        form = PedidoArticulosForm()
    return render(request, 'AppTienda/formulario_pedido.html', {'form': form})

@login_required
def agregarArticulosPedido(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticulosForm()
    return render(request, 'AppTienda/formulario_articulospedido.html', {'form': form})




# def crear_vehiculos(request):
#     if request.method == 'POST':
#         form = CrearPosteo(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('inicio')
#     else:
#         form = CrearPosteo()
#     return render(request, 'AppTienda/formulario_posteo.html', {'form': form})