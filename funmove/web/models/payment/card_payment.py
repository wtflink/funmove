# -*- coding: utf-8 -*-
from django.db import models
from payment_records import PaymentRecords
from credit_card_type import CreditCardType
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
