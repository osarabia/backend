# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Gastos(models.Model):
    fecha = models.DateTimeField(auto_now=False, null=False, blank=False)
    concepto = models.CharField(max_length=60, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    user_id = models.ForeignKey(User)

    class Meta:
        unique_together = (('user_id', 'fecha'),)
        db_table = 'gastos'
