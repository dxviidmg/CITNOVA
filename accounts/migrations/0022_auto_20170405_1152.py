# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20170405_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Arq.', 'Arq.'), ('T. S. U.', 'T. S. U.'), ('Tec.', 'Tec.'), ('Mtro(a).', 'Mtro(a).'), ('Dr.', 'Dr.'), ('Lic.', 'Lic.'), ('Ing.', 'Ing.')], default='C.', max_length=30),
        ),
    ]
