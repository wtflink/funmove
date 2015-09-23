# -*- coding: utf-8 -*-
# 搬運需求
from django.db import models

class MovingRequire(models.Model):
	# TOOD : DriverExpection 由於django尚不支援 BigInt Auto_increment，所以後續要處理
	id = models.BigIntegerField(primary_key=True)
	floor = models.IntegerField(default=1)
	elevator = models.BooleanField(default=None)

	class Meta:
		db_table = 'Moving_Require'