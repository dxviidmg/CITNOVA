# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20170403_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Arq.', 'Arq.'), ('Ing.', 'Ing.'), ('T. S. U.', 'T. S. U.'), ('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
