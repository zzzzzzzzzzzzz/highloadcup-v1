# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0004_auto_20170902_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
