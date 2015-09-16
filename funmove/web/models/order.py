# -*- coding: utf-8 -*-
from django.db import models
from member import UserInfo, DriverInfo,GroupInfo
from payment import PaymentRecords

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
        related_name='Orders'
    )
    # 使用者外鍵
    fk_user_info = models.ForeignKey(
        'UserInfo',
        related_name='Orders'
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

# 訂單狀態
# TODO : OrderState 需補上後台資料，目前有 預約中，運送中，運送完畢
class OrderState(models.Model):
    # 狀態
    state = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  OrderState 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Order_Status'

# 訂單細節
class OrderDetail(models.Model):
    # TODO : OrderDetail 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 描述 或是作為 備註欄
    description = models.CharField(max_length=255)
    # 以下為目前可預測之搬運品項．預設為0，統計數量
    # 項目：機車
    item_motor = models.IntegerField(default=0)
    # 項目：家寵
    item_pet = models.IntegerField(default=0)
    # 項目：單人床
    item_single_bed = models.IntegerField(default=0)
    # 項目：雙人床
    item_twin_bed = models.IntegerField(default=0)
    # 項目：書櫃
    item_bookcase = models.IntegerField(default=0)
    # 項目：櫃子
    item_cupboard = models.IntegerField(default=0)
    # 項目：桌子
    item_table = models.IntegerField(default=0)
    # 項目：椅子
    item_chair = models.IntegerField(default=0)
    # 項目：冰箱
    item_refrigerator = models.IntegerField(default=0)
    # 項目：沙發
    item_sofa = models.IntegerField(default=0)
    # 項目：易碎品
    item_fragile = models.IntegerField(default=0)
    # 其他品項，透過字串文字輸入，並以,分隔
    item_Other = models.CharField(max_length=255)

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : OrderDetail 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Order_Detail'

# 優惠記錄
class BonusRecord(models.Model):
    # 序號
    # TODO : 需要設計一組演算加密解密法（後期）
    serial = models.CharField(max_length=255)
    # 外鍵，屬於哪位使用者的優惠記錄，使用者可以得知所有他的優惠記錄
    fk_user_info = models.ForeignKey(
        'UserInfo',
        related_name='bonus_records'
    )
    # 外鍵，得知屬於的優惠類型，優惠類型可以反查到所有釋放出去的優惠
    fk_bonus_type = models.ForeignKey('BonusType', related_name='bonus')
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
