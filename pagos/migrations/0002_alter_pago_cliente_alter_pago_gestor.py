# Generated by Django 5.0.7 on 2024-07-13 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_rut'),
        ('gestores', '0001_initial'),
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='gestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='gestores.gestor'),
        ),
    ]
