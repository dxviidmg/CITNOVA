# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20170228_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='metodo_pago',
            field=models.CharField(choices=[('TRANSFERENCIA ELECTRÓNICA', 'TRANSFERENCIA ELECTRÓNICA'), ('CHEQUE', 'CHEQUE')], max_length=30),
        ),
    ]
