# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170307_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('T. S. U.', 'T. S. U.'), ('Mtro(a).', 'Mtro(a).'), ('Ing.', 'Ing.'), ('Tec.', 'Tec.'), ('Dr.', 'Dr.'), ('Lic.', 'Lic.'), ('Arq.', 'Arq̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣.')], default='C.', max_length=30),
        ),
    ]
