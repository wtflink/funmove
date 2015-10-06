# -*- coding: utf-8 -*-
from django.db import models

# 駕照種類與各種可以駕駛的車種
# TODO ：DrivingLicneseCategory 需後台建檔資料
class DrivingLicenseCategory(models.Model):
    # 類型名稱
    type_name = models.CharField(max_length=45)
    # 可否營業，預設為不可，會依照卡片的類型
    business = models.BooleanField(default=False)
    # 可以行駛的車種，一定要建檔，True表示可以，反之不行
    # 大貨車
    LargeTrucks = models.BooleanField(null=False, blank=False, default=None)
    # 連結車
    Trailer = models.BooleanField(null=False, blank=False, default=None)
    # 大客車
    Bus = models.BooleanField(null=False, blank=False, default=None)
    # 小型車
    Van = models.BooleanField(null=False, blank=False, default=None)
    # 大型重型機車
    LargeHeavyMotorcycle = models.BooleanField(null=False, blank=False, default=None)
    # 普通重型機車
    OriginalHeavyMotorcycle = models.BooleanField(null=False, blank=False, default=None)
    # 普通輕型機車
    LightMotorcycle = models.BooleanField(null=False, blank=False, default=None)
    # 小型輕型機車
    SmallLightMotorcycle = models.BooleanField(null=False, blank=False, default=None)

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  VehiDrivingLicneseCategorycleBand 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Driving_Licnese_Category'