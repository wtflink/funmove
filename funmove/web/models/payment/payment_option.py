# -*- coding: utf-8 -*-
from django.db import models

# 付款的方式選擇
# TODO : PaymentOption 資料後台建置
class PaymentOption(models.Model):
    # 付款方式，目前包含，面交，信用卡，超商付款
    choice = models.CharField(max_length=45, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  PaymentOption 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Payment_Option'

    def __unicode__(self):
        pass
