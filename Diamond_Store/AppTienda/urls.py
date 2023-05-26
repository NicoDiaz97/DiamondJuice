from django.contrib import admin
from django.urls import path
from AppTienda.views import galeria_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', galeria_productos, name='galeria-productos')
]