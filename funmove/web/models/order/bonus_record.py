# -*- coding: utf-8 -*-
from django.db import models
from web.models.member.user_info import UserInfo
from web.models.member.group_info import GroupInfo
from bonus_type import BonusType

# 優惠記錄
class BonusRecord(models.Model):
	# 序號
	# TODO : 需要設計一組演算加密解密法（後期）
	serial = models.CharField(max_length=255)
	# 外鍵，得知屬於的優惠類型，優惠類型可以反查到所有釋放出去的優惠
	fk_bonus_type = models.ForeignKey('BonusType', related_name='bonus')
	# 每一筆記錄可能是一般使用者 或是 團體使用者 ，因此外鍵可以null
	# 外鍵，屬於哪位使用者的優惠記錄，使用者可以得知所有他的優惠記錄
	fk_user_info = models.ForeignKey(
		'UserInfo',
		related_name='bonus_records',
		null=True,
		# 不被 CASCADE 影響，變成NULL 如果有設定NULL
		on_delete=models.SET_NULL
	)

	# 外鍵，屬於哪位團體的付款記錄
	fk_group_info = models.ForeignKey(
		'GroupInfo',
		related_name='bonus_records',
		null=True,
		# 不被 CASCADE 影響，變成NULL 如果有設定NULL
		on_delete=models.SET_NULL
	)

	# 使用的日期，預設為null，等到使用了才改為有時間
	used_date = models.DateTimeField(null=True)
	# 是否已經使用，預設為沒有 False
	is_used = models.BooleanField(default=False)

	create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	delete_date = models.DateTimeField(blank=True, null=True)
	# 是否被刪除的註記
	deactivated = models.BooleanField(default=False)
	# 帳號可能是使用者或是後台帳號
	# TODO : BonusRecord 需要調整此部分的 新增與修改判斷
	create_account = models.CharField(max_length=45, null=False)
	update_account = models.CharField(max_length=45, null=False)
	deactivated_account = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		db_table = 'Bonus_Record'
