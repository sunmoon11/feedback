# -*- coding: utf-8 -*-

from django.db import models


class FeedbackStatus(models.Model):
    fds_content = models.TextField(verbose_name=u"Сообщение", null=True, blank=True)
    fds_from = models.EmailField(verbose_name=u"Эл. Почта", null=True, blank=True)
    fds_status = models.BooleanField(verbose_name=u"Статус", default=False)

    fds_create_time = models.DateTimeField(verbose_name=u"Create Time", auto_now_add=True)
    fds_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Feedback"
