# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0029_auto_20170412_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='metodo_pago',
            field=models.CharField(choices=[('TRANSFERENCIA ELECTRÓNICA', 'TRANSFERENCIA ELECTRÓNICA'), ('CHEQUE', 'CHEQUE')], max_length=30),
        ),
    ]
