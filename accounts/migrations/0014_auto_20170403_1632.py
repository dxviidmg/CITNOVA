# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20170403_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).'), ('Arq.', 'Arq.'), ('T. S. U.', 'T. S. U.'), ('Ing.', 'Ing.')], default='C.', max_length=30),
        ),
    ]
