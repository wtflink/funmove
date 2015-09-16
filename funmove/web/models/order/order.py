# -*- coding: utf-8 -*-
from django.db import models
from web.models.member.user_info import UserInfo
from web.models.member.group_info import GroupInfo
from web.models.member.driver_info import DriverInfo
from order_state import OrderState
from web.models.payment.payment_records import PaymentRecords

# 訂單
class Order(models.Model):
    # TODO : Order 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 搬運日期
    reservation_date = models.DateField(null=False, blank=False)
    # 搬運時間
    reservation_time = models.TimeField(null=False, blank=False)
    # 搬運地點
    departure = models.CharField(max_length=255)
    # 目的地點
    destination = models.CharField(max_length=255)
    # 車資，可以為null，等到搬運完後才得知實際金錢
    wage = models.IntegerField(default=0)
    # 司機外鍵
    fk_driver = models.ForeignKey(
        'DriverInfo',
        related_name='orders'
    )
    # 兩者只會有一個外鍵，因此可以為 Null
    # 使用者外鍵
    fk_user_info = models.ForeignKey(
        'UserInfo',
        related_name='orders',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 團體外鍵
    fk_group_info = models.ForeignKey(
        'GroupInfo',
        related_name='orders',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 訂單細節外鍵
    fk_detail = models.OneToOneField('OrderDetail', to_field=None)
    # 1-1外鍵，付款資料，每筆付款記錄只會對應到一筆訂單，每一筆訂單會對
    fk_payment_record = models.OneToOneField(
        'PaymentRecords',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 訂單狀態
    fk_state = models.ForeignKey(
        'OrderState',
        related_name='orders'
    )

    class Meta:
        db_table = 'Order'
