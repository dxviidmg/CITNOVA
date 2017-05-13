# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0070_auto_20170510_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(choices=[('P. Física', 'P. Física'), ('P. Moral', 'P. Moral')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('T. S. U.', 'T. S. U.'), ('Ing.', 'Ing.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).'), ('Tec.', 'Tec.'), ('Arq.', 'Arq.'), ('Lic.', 'Lic.')], default='C.', max_length=30),
        ),
    ]