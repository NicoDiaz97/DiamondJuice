from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    imagen          = models.ImageField(upload_to='imagenes_productos', blank=True)
    nombre          = models.CharField(max_length = 64)
    descripcion     = models.CharField(max_length = 1000)
    tipo            = models.CharField(max_length = 64)
    cant_nicotina   = models.IntegerField()
    stock           = models.IntegerField()
    precio_min      = models.IntegerField()
    precio_may      = models.IntegerField()
    cant_min_may    = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Pedido(models.Model):
    user                    = models.ForeignKey(User,on_delete=models.CASCADE)
    tipo_retiro             = models.CharField(max_length=100)
    direccion_envio         = models.CharField(max_length=1000, blank=True)
    comentarios_adicionales = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f('Pedido Nro: {self.id} - Usuario: {self.user}')

class ArticulosPedido(models.Model):
    usuario_pedido_id   = models.ForeignKey(User,on_delete=models.CASCADE)
    pedido_id           = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    producto            = models.ForeignKey(Producto,on_delete=models.SET_NULL, null=True)
    cantidad            = models.IntegerField()

    