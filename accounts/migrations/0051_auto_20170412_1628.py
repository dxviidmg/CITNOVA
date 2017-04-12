# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20170412_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(choices=[('P. Física', 'P. Física'), ('P. Moral', 'P. Moral')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Mtro(a).', 'Mtro(a).'), ('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('Dr.', 'Dr.'), ('Arq.', 'Arq.'), ('Ing.', 'Ing.'), ('T. S. U.', 'T. S. U.')], default='C.', max_length=30),
        ),
    ]
