# Generated by Django 4.2.1 on 2023-05-29 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0006_producto_tamanio_alter_pedido_direccion_envio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulospedido',
            name='usuario_pedido_id',
        ),
    ]
