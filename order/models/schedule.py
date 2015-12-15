# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class timeofaday(models.Model):
	time = models.TimeField(blank=False)

class Schedule(models.Model):

    reservation_date = models.DateField(default = datetime.now, null=False, blank=False)
    reservation_time = models.ForeignKey('timeofaday', on_delete=models.CASCADE)
