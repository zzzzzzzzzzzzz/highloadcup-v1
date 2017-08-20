# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    place = models.TextField(
        u'Описание достопримечательности'
    )

    country = models.CharField(
        u'Страна расположения',
        max_length=50
    )

    city = models.CharField(
        u'Город расположения',
        max_length=50
    )

    distance = models.PositiveIntegerField(
        u'Расстояние в километрах',
    )

    def __unicode__(self):
        return self.city + ' ' + self.country

    class Meta:
        verbose_name = u'Достопримечательность'
        verbose_name_plural = u'Достопримечательности'
