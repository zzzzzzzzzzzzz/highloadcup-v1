# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438')),
                ('country', models.CharField(max_length=50, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
                ('city', models.CharField(max_length=50, verbose_name='\u0413\u043e\u0440\u043e\u0434 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
                ('distance', models.PositiveIntegerField(verbose_name='\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0432 \u043a\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u0430\u0445')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u0414\u043e\u0441\u0442\u043e\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438',
            },
        ),
    ]