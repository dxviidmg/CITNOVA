# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0039_auto_20170503_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='cuenta_bancaria_del_programa',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
