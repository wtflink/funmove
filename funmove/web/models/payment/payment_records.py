# -*- coding: utf-8 -*-
from django.db import models
from payment_option import PaymentOption
from web.models.member.user_info import UserInfo
from web.models.member.group_info import GroupInfo

# 付款記錄
class PaymentRecords(models.Model):
	# 外鍵，屬於哪種付款選項，付款選項對應到的所有此付款模式的付款紀錄
	fk_payment_option = models.ForeignKey(
		'PaymentOption',
		related_name='payment_records'
	)
	# 兩者只會有一個外鍵，因此可以為 Null
	# 外鍵，屬於哪位使用者的付款記錄
	fk_user_info = models.ForeignKey(
		'UserInfo',
		related_name='payment_records',
		null=True,
		# 不被 CASCADE 影響，變成NULL 如果有設定NULL
		on_delete=models.SET_NULL
	)
	# 外鍵，屬於哪位團體的付款記錄
	fk_group_info = models.ForeignKey(
		'GroupInfo',
		related_name='payment_records',
		null=True,
		# 不被 CASCADE 影響，變成NULL 如果有設定NULL
		on_delete=models.SET_NULL
	)

	create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	delete_date = models.DateTimeField(blank=True, null=True)
	# 是否被刪除的註記
	deactivated = models.BooleanField(default=False)
	# 帳號可能是使用者或是後台帳號
	# TODO :  PaymentRecords 需要調整此部分的 新增與修改判斷
	create_account = models.CharField(max_length=45, null=False)
	update_account = models.CharField(max_length=45, null=False)
	deactivated_account = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		db_table = 'Payment_Records'

	def __unicode__(self):
		pass
