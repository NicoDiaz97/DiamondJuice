from django.shortcuts import render
from AppTienda.models import Producto

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

def crear_pedido(request):
    if request.method == 'POST':
        data = request.POST
        
    
    