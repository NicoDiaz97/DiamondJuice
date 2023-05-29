# Generated by Django 4.2.1 on 2023-05-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0005_pedido_articulospedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tamanio',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='direccion_envio',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
