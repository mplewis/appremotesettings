# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appremotesettings', '0004_add_verbose_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='datatype',
            field=models.IntegerField(choices=[(1, 'Boolean'), (2, 'Integer'), (3, 'Float'), (4, 'String'), (5, 'Date')], default=1, verbose_name='data type'),
        ),
    ]
