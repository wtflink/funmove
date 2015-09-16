# -*- coding: utf-8 -*-
from django.db import models

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
