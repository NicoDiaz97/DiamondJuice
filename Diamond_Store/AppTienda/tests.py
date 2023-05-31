
from django.test import TestCase
from AppTienda.models import Producto

class ProductoTestCase(TestCase):
    def setUp(self):
        # Crear algunos productos de prueba
        Producto.objects.create(
            imagen = "imagen1.jpg",
            nombre = "Producto 1",
            descripcion = "Este es el producto 1",
            tipo = "Tipo 1",
            tamanio = "Grande",
            cant_nicotina = 10,
            stock = 100,
            precio_min = 50,
            precio_may = 40,
            cant_min_may = 10
        )
        Producto.objects.create(
            imagen = "imagen2.jpg",
            nombre = "Producto 2",
            descripcion = "Este es el producto 2",
            tipo = "Tipo 2",
            tamanio = "Mediano",
            cant_nicotina = 5,
            stock = 50,
            precio_min = 30,
            precio_may = 25,
            cant_min_may = 5
        )

    def test_producto_str(self):
        # Probar el método __str__ del modelo Producto
        producto1 = Producto.objects.get(nombre="Producto 1")
        producto2 = Producto.objects.get(nombre="Producto 2")
        self.assertEqual(str(producto1), "Producto 1")
        self.assertEqual(str(producto2), "Producto 2")

    def test_producto_precio(self):
        # Probar que el precio mayorista sea menor que el precio minorista
        producto1 = Producto.objects.get(nombre="Producto 1")
        producto2 = Producto.objects.get(nombre="Producto 2")
        self.assertLess(producto1.precio_may, producto1.precio_min)
        self.assertLess(producto2.precio_may, producto2.precio_min)

    def test_producto_stock(self):
        # Probar que el stock sea mayor o igual que cero
        producto1 = Producto.objects.get(nombre="Producto 1")
        producto2 = Producto.objects.get(nombre="Producto 2")
        self.assertGreaterEqual(producto1.stock, 0)
        self.assertGreaterEqual(producto2.stock, 0)