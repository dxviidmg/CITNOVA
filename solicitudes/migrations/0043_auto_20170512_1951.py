# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0042_auto_20170510_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='metodo_pago',
            field=models.CharField(choices=[('CHEQUE', 'CHEQUE'), ('TRANSFERENCIA ELECTRÓNICA', 'TRANSFERENCIA ELECTRÓNICA')], max_length=30),
        ),
    ]
