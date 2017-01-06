# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.DecimalField(decimal_places=2, max_digits=10)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
    ]