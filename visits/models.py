# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from locations.models import Location

from users.models import User

MARKS = (
    (0, u'Треш'),
    (1, u'Отстой'),
    (2, u'С пивом потянет'),
    (3, u'Потянет и без пива'),
    (4, u'Нарм'),
    (5, u'Отлично')
)


class Visit(models.Model):
    location = models.ForeignKey(
        Location
    )

    user = models.ForeignKey(
        User
    )

    visited_at = models.IntegerField(
        u'Дата посещения',
        db_index=True,
        default=0
    )

    mark = models.PositiveSmallIntegerField(
        u'Оценка посещения',
        choices=MARKS,
        default=2
    )

    def __unicode__(self):
        return self.location.country + ' ' + self.location.city

    class Meta:
        verbose_name = u'Посещение'
        verbose_name_plural = u'Посещения'
        ordering = ['-visited_at']

