# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20170412_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Ing.', 'Ing.'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('T. S. U.', 'T. S. U.'), ('Lic.', 'Lic.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
