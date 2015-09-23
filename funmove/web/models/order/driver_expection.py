# -*- coding: utf-8 -*-
# 期望的司機類型
from django.db import models

class DriverExpection(models.Model):
	# TOOD : DriverExpection 由於django尚不支援 BigInt Auto_increment，所以後續要處理
	id = models.BigIntegerField(primary_key=True)
	gender = models.BooleanField(default=None)
	talkative = models.BooleanField(default=None)
	other = models.CharField(max_length=255)
	speak_eng = models.BooleanField(default=None)

	class Meta:
		db_table = 'Driver_Expection'