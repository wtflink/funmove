# -*- coding: utf-8 -*-
from django.db import models
from member.models import UserInfo, GroupInfo, DriverInfo
from order_state import OrderState
from payment.models import PaymentRecords
from moving_require import MovingRequire
from driver_expection import DriverExpection
from datetime import datetime
from django.core.validators import MinLengthValidator


# 訂單
class Orders(models.Model):
    MIN_CHOICES= ((0,0), (30,30))
    HR_CHOICES = [(i,i) for i in range(7)]
    year_choices=[(i, i) for i in range(1910, int(datetime.now().year) + 1)]
    mon_choices=[(i, i) for i in range(1, 13)]
    day_choices=[(i, i) for i in range(1, 32)]
    # TODO : Order 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.AutoField(primary_key=True)
    # 搬運日期
    reservation_date = models.DateField(default = datetime.now, null=False, blank=False)
    # 搬運時間(time that start the service) /?choices needed?/
    reservation_time = models.TimeField(default = '12:00',null=False, blank=False)
    #服務時間(store an int which indicate the length of the service)
    time_needed_hr = models.IntegerField(choices = HR_CHOICES, default = 0,null = False, blank = False)
    time_needed_min= models.IntegerField(choices = MIN_CHOICES, default = 0,null = False, blank = False)
    # 搬運地點
    departure = models.CharField(max_length=255)
    # 目的地點
    destination = models.CharField(max_length=255)
    # 車資，可以為null，等到搬運完後才得知實際金錢
    wage = models.IntegerField(default=0)

    name = models.CharField(max_length=45, default = None, null=False, blank=False)
    email = models.EmailField(default = None,null=False, blank=False)
    cell_phone = models.CharField(validators=[MinLengthValidator(10)], max_length=11, null=False, blank=False, default =None,)
    # 出生日
    birth_year = models.IntegerField(
        max_length=4,
        default=None, blank=False, null=True, choices = year_choices,)
    birth_month = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=True, choices = mon_choices,)
    birth_day = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=True, choices = day_choices,)

    remarks = models.TextField(max_length=200, default = None)

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)    

    confirmation_key = models.CharField(max_length=40, default = None, blank=True)
    key_expires = models.DateTimeField(default=datetime.now)
    is_confirmed = models.BooleanField(default = False)


    # 司機外鍵
    #fk_driver = models.ForeignKey(
    #    'member.DriverInfo',
    #    related_name='orders',
    #    null=True,
    #    # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)
    # 兩者只會有一個外鍵，因此可以為 Null
    # 使用者外鍵
    #fk_user_info = models.ForeignKey(
    #    'member.UserInfo',
    #    related_name='orders',
    #    null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)
    # 團體外鍵
    #fk_group_info = models.ForeignKey(
    #    'member.GroupInfo',
    #    related_name='orders',
    #    null=True,
    #    # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)
    # 訂單細節外鍵
    #fk_detail = models.OneToOneField('OrderDetail')
    # 1-1外鍵，付款資料，每筆付款記錄只會對應到一筆訂單，每一筆訂單會對
    #fk_payment_record = models.OneToOneField(
    #    'payment.PaymentRecords',
    #    null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)
    # 訂單狀態
    #fk_state = models.ForeignKey(
    #    'OrderState',
    #    related_name='orders'
    #)
    # 期望司機類型，1-1外鍵
    #fk_driver_expection = models.OneToOneField(
    #    'DriverExpection',
    #    null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)
    # 搬運需求
    #fk_moving_require = models.OneToOneField(
    #    'MovingRequire',
    #    null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
    #    on_delete=models.SET_NULL
    #)

    class Meta:
        db_table = 'Orders'
