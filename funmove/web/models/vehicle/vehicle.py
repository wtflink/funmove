# -*- coding: utf-8 -*-
from django.db import models
from web.models.member.driver_info import DriverInfo
from vehicle_band_model import VehicleBandModel
from driving_license import DrivingLicnese
from police_clearance import PoliceClearance
from compulsory_insurance import CompulsoryInsurance
from vehicle_license import VehicleLicense
from vehicle_plate import VehiclePlate

# 車輛
class Vehicle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # 此台車的款型品牌，如果要找品牌，再從Model的外鍵去找到所屬品牌 以及 車種
    fk_band_model = models.ForeignKey(
        'VehicleBandModel',
        related_name='vehicles',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，關聯到司機
    fk_driver = models.ForeignKey(
        'DriverInfo',
        related_name='vehicles',
    )
    # 外鍵，駕照資料，司機也可以得知使用此駕照開的所有車輛
    fk_driving_license = models.ForeignKey(
        'DrivingLicnese',
        related_name='vehicles',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 車的配件，使用字串與逗號記錄各個名稱
    accessories = models.CharField(max_length=255, null=True)
    # 外鍵，關聯到良民證，可以為 null 因為不一定會有(加強驗證)
    fk_police_clearance = models.ForeignKey(
        'PoliceClearance',
        related_name='vehicles',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，汽車強制則責任險，可以為 null 因為不一定會有(加強驗證)
    fk_compulsory_insurance = models.ForeignKey(
        'CompulsoryInsurance',
        related_name='vehicles',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，汽車行照，可以為 null 因為不一定會有(加強驗證)
    fk_vehicle_license = models.ForeignKey(
        'VehicleLicense',
        related_name='vehicles',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，汽車牌照，不可為null，一定至少要打車牌，否則無法建檔，圖片可以之後再上傳驗證
    fk_vehicle_plate = models.ForeignKey(
        'VehiclePlate',
        related_name='vehicles',
    )

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : Vehicle 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle'
