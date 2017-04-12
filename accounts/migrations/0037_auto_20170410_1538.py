# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20170406_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='RFC',
            field=models.FileField(upload_to='RFC/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Mtro(a).', 'Mtro(a).'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('Dr.', 'Dr.'), ('T. S. U.', 'T. S. U.'), ('Ing.', 'Ing.'), ('Lic.', 'Lic.')], default='C.', max_length=30),
        ),
    ]
