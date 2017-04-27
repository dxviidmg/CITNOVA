# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_auto_20170427_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='telefono',
            new_name='teléfono',
        ),
        migrations.AlterField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(choices=[('P. Moral', 'P. Moral'), ('P. Física', 'P. Física')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Ing.', 'Ing.'), ('Arq.', 'Arq.'), ('Lic.', 'Lic.'), ('Tec.', 'Tec.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).'), ('T. S. U.', 'T. S. U.')], default='C.', max_length=30),
        ),
    ]
