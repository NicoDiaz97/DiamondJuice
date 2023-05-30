# Generated by Django 4.2.1 on 2023-05-30 02:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0007_remove_articulospedido_usuario_pedido_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_retiro',
            field=models.CharField(choices=[('D', 'Envío a domicilio'), ('R', 'Retiro en sucursal')], max_length=100),
        ),
    ]
