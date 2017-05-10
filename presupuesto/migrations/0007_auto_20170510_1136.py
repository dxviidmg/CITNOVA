# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0006_auto_20170510_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='monto_2t_amplicacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_2t_autorizado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_2t_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_2t_modificado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_2t_por_ejercer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_2t_reduccion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_amplicacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_autorizado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_modificado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_por_ejercer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_3t_reduccion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_amplicacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_autorizado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_modificado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_por_ejercer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_4t_reduccion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
    ]
