# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0068_auto_20170505_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Tec.', 'Tec.'), ('Lic.', 'Lic.'), ('T. S. U.', 'T. S. U.'), ('Ing.', 'Ing.'), ('Dr.', 'Dr.'), ('Arq.', 'Arq.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
