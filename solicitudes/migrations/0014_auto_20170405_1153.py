# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0013_auto_20170405_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='mes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mes', to='presupuesto.Mes'),
        ),
    ]