# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20161206_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='latitude',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='tour',
            name='longitude',
            field=models.CharField(max_length=25),
        ),
    ]
