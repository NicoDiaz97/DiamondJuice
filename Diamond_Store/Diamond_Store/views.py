from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppTienda/inicio.html',
        context=contexto,
    )
    return http_response

def acerca_de_mi(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppTienda/about-me.html',
        context=contexto,
    )
    return http_response
