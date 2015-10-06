# -*- coding: utf-8 -*-
from django.db import models

# 優惠類型
# TODO : 由後台系統建立
class BonusType(models.Model):
    # 目前有：1.則扣，2.贈送金額，3.免費使用
    type_name = models.CharField(max_length=45)
    # 根據優惠類型，提供的資料，為數值，Ex：類型1 => 扣0.8折；2.贈送金額 =>200
    item = models.FloatField(default=0.0)
    # 發送單位，由哪個單位的名義發送此優惠訊息
    send_organization = models.CharField(max_length=45)
    # 優惠名稱
    name = models.CharField(max_length=45)
    # 優惠內容
    content = models.TextField()
    # 優惠的期限，不可為null
    deadline = models.DateTimeField(null=False)

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : BonusType 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Bonus_Type'
