# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
    

class Documents(models.Model):
    upload_by = models.ForeignKey(User, related_name='upload_by')
    datestamp = models.DateTimeField(auto_now_add=True) 
    process = models.BooleanField(default=False)
    document = models.FileField(upload_to='uploads', default=1)

    class Meta:
        db_table = 'uploads'
