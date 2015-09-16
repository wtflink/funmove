# -*- coding: utf-8 -*-
from django.db import models

# 記錄各類信用卡的資訊
# TODO : CreditCardType 資料後台建置
class CreditCardType(models.Model):
    # 卡類名稱
    type_name = models.CharField(max_length=45)
    # 驗證碼長度
    security_code_length = models.IntegerField()
    # 卡片長度
    card_length = models.IntegerField()
    # 卡片的起始數字，如果有逗號，表示還有數值，如果用 - 表示是一個範圍
    card_begin_number = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO : CreditCardType 建立與更新，需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Credit_Card_Type'