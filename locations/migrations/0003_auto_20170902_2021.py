# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20170827_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
