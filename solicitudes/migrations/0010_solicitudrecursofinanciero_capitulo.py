# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0002_programa_departamento'),
        ('solicitudes', '0009_auto_20170404_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudrecursofinanciero',
            name='capitulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Capitulo', to='presupuesto.Capitulo'),
        ),
    ]
