# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel
from model_utils.fields import SplitField


class Post(TimeStampedModel, models.Model):
    titulo = models.CharField(max_length=100)
    corpo = SplitField()

    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.titulo
