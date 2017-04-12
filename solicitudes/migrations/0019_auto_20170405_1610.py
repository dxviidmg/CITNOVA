# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0018_delete_comprobantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('no_factuta', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=20)),
                ('scan', models.ImageField(upload_to='comprobantes/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='solicitudrecursofinanciero',
            name='metodo_pago',
            field=models.CharField(choices=[('CHEQUE', 'CHEQUE'), ('TRANSFERENCIA ELECTRÓNICA', 'TRANSFERENCIA ELECTRÓNICA')], max_length=30),
        ),
        migrations.AddField(
            model_name='comprobantes',
            name='srf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SRF', to='solicitudes.SolicitudRecursoFinanciero'),
        ),
    ]