# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_news', models.ImageField(null=True, upload_to='images/news', verbose_name='Image')),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Content')),
                ('status', models.CharField(choices=[('unpublish', 'Unpublish'), ('publish', 'Publish')], default='unpublish', max_length=10)),
                ('publish', models.DateField()),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]