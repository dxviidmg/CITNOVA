# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0027_auto_20170412_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitudrecursofinanciero',
            old_name='comprobantes',
            new_name='comprobante',
        ),
    ]
