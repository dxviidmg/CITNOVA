# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_auto_20170503_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Mtro(a).', 'Mtro(a).'), ('Ing.', 'Ing.'), ('T. S. U.', 'T. S. U.'), ('Dr.', 'Dr.'), ('Lic.', 'Lic.'), ('Arq.', 'Arq.'), ('Tec.', 'Tec.')], default='C.', max_length=30),
        ),
    ]
