# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomania', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
