# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170228_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('T. S. U.', 'T. S. U.'), ('Arq.', 'Arq̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣̣.'), ('Ing.', 'Ing.'), ('Mtro(a).', 'Mtro(a).')], default='C.', max_length=30),
        ),
    ]
