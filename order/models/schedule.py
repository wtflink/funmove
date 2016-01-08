# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class timeofaday(models.Model):
	time = models.TimeField(blank=False)

class Schedule(models.Model):

	id = models.AutoField(primary_key=True)
	reservation_start = models.DateTimeField(default = datetime.now,null=False, blank=False)
	reservation_end = models.DateTimeField(default=datetime.now,null=False, blank=False)
	title = models.CharField(max_length=45, default = None, null=False, blank=False)
	is_cancelled = models.BooleanField(default = False)
