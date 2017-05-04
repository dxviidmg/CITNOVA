# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0065_auto_20170503_1503'),
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
            field=models.CharField(blank=True, choices=[('T. S. U.', 'T. S. U.'), ('Mtro(a).', 'Mtro(a).'), ('Dr.', 'Dr.'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('Lic.', 'Lic.'), ('Ing.', 'Ing.')], default='C.', max_length=30),
        ),
    ]
