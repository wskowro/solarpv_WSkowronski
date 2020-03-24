# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    client = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    product = models.CharField(max_length=40)
    testStandard = models.CharField(max_length=40)
    certificate = models.CharField(max_length=40)
