# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appremotesettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='datatype',
            field=models.IntegerField(choices=[(1, 'Boolean'), (2, 'Integer'), (3, 'Float'), (4, 'String')], default=1),
        ),
    ]
