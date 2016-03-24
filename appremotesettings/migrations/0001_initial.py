# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('value', models.TextField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appremotesettings.App')),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('key', models.TextField()),
                ('value', models.TextField()),
                ('datatype', models.IntegerField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appremotesettings.App')),
            ],
        ),
    ]