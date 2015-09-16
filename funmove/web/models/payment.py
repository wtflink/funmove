# -*- coding: utf-8 -*-
from django.db import models
from member import UserInfo

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

# 付款記錄
class PaymentRecords(models.Model):
    # 外鍵，屬於哪種付款選項，付款選項對應到的所有此付款模式的付款紀錄
    fk_payment_option = models.ForeignKey('PaymentOption', related_name='payment_records')
    # 外鍵，屬於哪位使用者的卡片記錄
    fk_user_info = models.ForeignKey('UserInfo', related_name='payments')
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

# 信用卡付款資訊
class CardPayment(models.Model):
    # TODO : CardPayment 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 由於各家卡片長度不一，統一用16(最長)
    card_number = models.CharField(max_length=16)
    # 由於驗證碼長度不一，先使用6碼
    security_code = models.CharField(max_length=6)
    # 外鍵，得知屬於卡個付款紀錄，每一筆付款記錄如果是卡片付款，只會對應一筆信用卡資訊
    fk_payment_record = models.OneToOneField(
        'PaymentRecords',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，屬於卡種類片類型，以及卡片的資料
    fk_card_type = models.ForeignKey(
        'CreditCardType',
        related_name='card_payments',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'Card_Payment'

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