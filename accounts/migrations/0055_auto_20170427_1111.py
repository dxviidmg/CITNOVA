# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_auto_20170420_1543'),
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
            field=models.CharField(blank=True, choices=[('T. S. U.', 'T. S. U.'), ('Dr.', 'Dr.'), ('Ing.', 'Ing.'), ('Mtro(a).', 'Mtro(a).'), ('Tec.', 'Tec.'), ('Lic.', 'Lic.'), ('Arq.', 'Arq.')], default='C.', max_length=30),
        ),
    ]
