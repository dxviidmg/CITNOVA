# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20170503_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Ing.', 'Ing.'), ('Arq.', 'Arq.'), ('Tec.', 'Tec.'), ('T. S. U.', 'T. S. U.'), ('Lic.', 'Lic.'), ('Mtro(a).', 'Mtro(a).'), ('Dr.', 'Dr.')], default='C.', max_length=30),
        ),
    ]