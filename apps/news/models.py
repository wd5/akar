# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from apps.common.models import PostBase


class News(PostBase):
    logo = models.ImageField(upload_to='news/logos/')

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})