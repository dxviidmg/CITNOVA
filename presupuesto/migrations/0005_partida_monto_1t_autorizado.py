# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0004_auto_20170505_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='monto_1t_autorizado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
    ]