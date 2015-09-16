# -*- coding: utf-8 -*-
from django.db import models
from member import DriverInfo

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

# 駕照種類與各種可以駕駛的車種
# TODO ：DrivingLicneseCategory 需後台建檔資料
class DrivingLicenseCategory(models.Model):
    # 類型名稱
    type_name = models.CharField(max_length=45)
    # 可否營業，預設為不可，會依照卡片的類型
    business = models.BooleanField(default=False)
    # 可以行駛的車種，一定要建檔，True表示可以，反之不行
    # 大貨車
    LargeTrucks = models.BooleanField(null=False, blank=False)
    # 連結車
    Trailer = models.BooleanField(null=False, blank=False)
    # 大客車
    Bus = models.BooleanField(null=False, blank=False)
    # 小型車
    Van = models.BooleanField(null=False, blank=False)
    # 大型重型機車
    LargeHeavyMotorcycle = models.BooleanField(null=False, blank=False)
    # 普通重型機車
    OriginalHeavyMotorcycle = models.BooleanField(null=False, blank=False)
    # 普通輕型機車
    LightMotorcycle = models.BooleanField(null=False, blank=False)
    # 小型輕型機車
    SmallLightMotorcycle = models.BooleanField(null=False, blank=False)

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
# 車的品牌
# TODO : VehicleBand 資料後台建置
class VehicleBand(models.Model):
    band_name = models.CharField(max_length=45, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  VehicleBand 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_Band'

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

# 車種(汽機車，大型貨車等等)
# TODO : VehicleCategory 資料後台建置
class VehicleCategory(models.Model):
    type_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO : VehicleCategory 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_Category'

# 交通工具配件
# TODO : VehicleAccessories 資料後台建置
class VehicleAccessories(models.Model):
    accessories_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  VehicleAccessories 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_Accessories'

# 良民證證明
class PoliceClearance(models.Model):
    # 上傳除片連結位置
    photo_url = models.ImageField(upload_to='upload/police_clearance_photo/')
    # 開始有效日期
    valid_begin_date = models.DateTimeField()
    # 截止有效日期
    valid_end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : PoliceClearance 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Police_Clearance'

# 汽車強制責任險證明
class CompulsoryInsurance(models.Model):
    # 上傳除片連結位置
    photo_url = models.ImageField(upload_to='upload/compulsory_insurance_photo/')
    # 開始有效日期
    valid_begin_date = models.DateTimeField()
    # 截止有效日期
    valid_end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : CompulsoryInsurance 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Compulsory_Insurance'

# 行照，表示這台車屬於誰
class VehicleLicense(models.Model):
    # 上傳除片連結位置
    photo_url = models.ImageField(upload_to='upload/vehicle_license_photo/')
    # 開始有效日期
    valid_begin_date = models.DateTimeField()
    # 截止有效日期
    valid_end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : VehicleLicense 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_License'

# 車牌
class VehiclePlate(models.Model):
    # 車牌號碼
    # TODO : 發現車牌因照年份與車種，有不同的驗證規則與類型，很繁瑣，是否需要再另外建置一個格式表格呢
    number = models.CharField(max_length=255, null=False)
    # 上傳除片連結位置
    photo_url = models.ImageField(upload_to='upload/vehicle_plate_photo/')
    # 開始有效日期
    valid_begin_date = models.DateTimeField()
    # 截止有效日期
    valid_end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : VehiclePlate 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vehicle_Plate'
