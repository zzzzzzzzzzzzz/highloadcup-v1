# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

class User(models.Model):
    email = models.CharField(
        u'Электронная почта',
        max_length=100,
        default=None
    #   unique=True # Уникальность гарантируется
    )

    first_name = models.CharField(
        u'Имя',
        max_length=50,
        default=None
    )

    last_name = models.CharField(
        u'Фамилия',
        max_length=50,
        default=None
    )

    gender = models.CharField(
        u'Пол',
        choices=GENDER_CHOICES,
        max_length=1,
        default='m'
    )

    birth_date = models.BigIntegerField(
        u'Дата рождения',
        default=0
    )

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'