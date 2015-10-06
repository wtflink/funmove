# -*- coding: utf-8 -*-
from django.db import models
from vehicle_band import VehicleBand
from vehicle_category import VehicleCategory
# 車的型號
# TODO : VehicleBandModel 資料後台建置
class VehicleBandModel(models.Model):
    # 車的型號
    model_name = models.CharField(max_length=45)
    # 外鍵，屬於哪種車的品牌，關聯到的車的品牌可以得知所有旗下的車型，須為 CASCADE
    fk_vehicle_band = models.ForeignKey(
        'VehicleBand',
        related_name='vehicle_models'
    )
    # 外鍵，此車屬於哪種運輸車種，一家品牌公司可能有多種不同種類的車種，如機車，汽車或大型貨車
    fk_vehicle_type = models.ForeignKey(
        'VehicleCategory',
        related_name='vehicle_models',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 頓數
    weight = models.IntegerField(null=False, blank=False)
    # 排氣量下限
    displacement_lower = models.IntegerField(null=False, blank=False)
    # 排氣量上限
    displacement_upper = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  VehicleBandModel 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_Band_Model'
