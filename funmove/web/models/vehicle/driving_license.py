# -*- coding: utf-8 -*-
from django.db import models
from web.models.member.driver_info import DriverInfo
from driving_license_category import DrivingLicenseCategory
# 駕照資料
class DrivingLicnese(models.Model):
    # TODO : DrivingLicnese 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 外鍵，屬於哪種駕照類型，以及可以行駛的車種資料，駕照種類關聯，可以取的有多少駕照
    fk_license_category = models.ForeignKey(
        'DrivingLicenseCategory',
        related_name='licenses',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，取得司機的關聯資料
    fk_driver = models.ForeignKey(
        'DriverInfo',
        related_name='lincenses',
    )
    # 發照日期資料
    publish_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : DrivingLicnese 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Driving_Licnese'