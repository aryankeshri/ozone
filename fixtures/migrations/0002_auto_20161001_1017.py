# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='score1',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='score2',
            field=models.CharField(default=None, max_length=2),
        ),
    ]
