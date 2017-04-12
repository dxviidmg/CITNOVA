# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0003_programa_cuenta_bancaria'),
        ('solicitudes', '0014_auto_20170405_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudrecursofinanciero',
            name='mes',
        ),
        migrations.AddField(
            model_name='solicitudrecursofinanciero',
            name='programa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programa', to='presupuesto.Programa'),
        ),
    ]