# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0058_auto_20170502_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Mtro(a).', 'Mtro(a).'), ('Lic.', 'Lic.'), ('T. S. U.', 'T. S. U.'), ('Dr.', 'Dr.'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('Ing.', 'Ing.')], default='C.', max_length=30),
        ),
    ]
