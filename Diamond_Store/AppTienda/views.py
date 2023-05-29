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

@login_required
def crearPedido(request):
    if request.method == 'POST':
        form    = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            return redirect('agregar-articulos', pedido.id )
        else:
            print(form.errors)
    else:
        form = PedidoForm()
    return render(request, 'AppTienda/formulario_pedido.html', {'form': form})

@login_required
def agregarArticulosPedido(request,id):
    if request.method == 'POST':
        print(request.POST.get('lista_articulos'))
        return redirect('inicio')
        # form    = ArticulosForm(request.POST)
        # if form.is_valid():
        #     pedido = form.save(commit=False)
        #     pedido.user = request.user
        #     pedido.save()
        #     return redirect('galeria-productos')
        # else:
        #     print(form.errors)
    else:
        form        = ArticulosForm()
        id_pedido   = id
        producto    = Producto.objects.all()
        return render(request, 'AppTienda/formulario_articulospedido.html', {'form' : form, 'id_pedido' : id_pedido, 'productos': producto})

def insert_articulos(request, pedido_id):
    # Obtener el pedido por su id o devolver un error 404 si no existe
    pedido = get_object_or_404(Pedido, id=pedido_id)
    # Si el request es POST, procesar el formulario
    if request.method == "POST":
        # Obtener los datos del formulario
        form = request.POST
        # Iterar sobre los datos del formulario para crear y asociar los articulos al pedido
        for i in range(len(form["nombre"])):
            nombre = form["nombre"][i]
            cantidad = form["cantidad"][i]
            precio = form["precio"][i]
            # Crear y asociar el articulo al pedido usando el método create
            pedido.articulospedido_set.create(cantidad=cantidad, precio=precio)
        # Redirigir a la vista del detalle del pedido
        return redirect("ver-pedido", pedido_id=pedido_id)
    # Si el request es GET, mostrar el formulario vacío
    else:
        # Renderizar el template con el pedido como contexto
        return render(request, "AppTienda/formulario_articulospedido.html", {"pedido": pedido})
    

def pedido_detail(request, pedido_id):
    # Obtener el pedido por su id o devolver un error 404 si no existe
    pedido = get_object_or_404(Pedido, id=pedido_id)
    # Obtener los articulos asociados al pedido
    articulos = pedido.articulospedido_set.all()
    # Renderizar el template con el pedido y los articulos como contexto
    return render(request, "AppTienda/pedido_detail.html", {"pedido": pedido, "articulos": articulos})

def create_order(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        articulos_formset = ArticulosPedidoFormSet(request.POST)
        if pedido_form.is_valid() and articulos_formset.is_valid():
            pedido = pedido_form.save()
            for articulo_form in articulos_formset:
                articulo = articulo_form.save(commit=False)
                articulo.pedido_id = pedido
                articulo.save()
            return redirect('galeria-productos')
    else:
        pedido_form = PedidoForm()
        articulos_formset = ArticulosPedidoFormSet(queryset=ArticulosPedido.objects.none())
        context = {"pedido_form": pedido_form, "articulos_formset": articulos_formset}
        return render(request, 'AppTienda/create_order.html', context)
        # articulos_formset = ArticulosPedidoFormSet(queryset=ArticulosPedido.objects.none())
        # context = {"pedido_form": pedido_form, "articulos_formset": articulos_formset}
        # context['articulos_empty_form'] = articulos_formset.empty_form
        # return render(request, 'AppTienda/create_order.html', context)
