# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20170405_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Ing.', 'Ing.'), ('T. S. U.', 'T. S. U.'), ('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
