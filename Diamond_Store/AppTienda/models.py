from django.db import models

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
