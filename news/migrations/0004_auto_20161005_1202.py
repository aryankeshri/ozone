# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
