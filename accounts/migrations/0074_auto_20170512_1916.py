# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0073_auto_20170510_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Ing.', 'Ing.'), ('Mtro(a).', 'Mtro(a).'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('T. S. U.', 'T. S. U.'), ('Lic.', 'Lic.'), ('Dr.', 'Dr.')], default='C.', max_length=30),
        ),
    ]