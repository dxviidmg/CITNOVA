# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20170412_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(choices=[('P. Moral', 'P. Moral'), ('P. Física', 'P. Física')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Tec.', 'Tec.'), ('Ing.', 'Ing.'), ('Lic.', 'Lic.'), ('Dr.', 'Dr.'), ('Arq.', 'Arq.'), ('T. S. U.', 'T. S. U.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
