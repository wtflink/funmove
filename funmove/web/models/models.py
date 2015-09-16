# -*- coding: utf-8 -*-
from django.db import models
from back_admin import BackAdmin
from facebook_account import FacebookAccount
from uuidfield import UUIDField


class MemebrType(models.Model):
    type_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO : MemebrType 建立與更新，需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Member_Type'

    def __unicode__(self):
        pass

class MemberAccount(models.Model):
    # TOOD : MemberAccount 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 可以使用 account 或是email 作為登入識別
    account = models.CharField(unique=True, max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    # 電話號碼
    cell_phone = models.CharField(max_length=11, null=False, blank=False)
    # 外鍵，關聯到 MemberType，可以知道屬於哪種MemberType
    # 透過related_name使得MemberType可以得知屬於此Type的MemebrAccount數量
    fk_member_type = models.ForeignKey(
        'MemebrType',
        related_name='type_accounts',
        null=True,
        on_delete=models.SET_NULL)
    # 是否有驗證過手機簡訊
    phone_sms_verification = models.BooleanField(default=False)
    # UUID產生驗證Key
    activation_key = UUIDField(auto=True)
    # 新增資料時會需要設定驗證的期限
    # 如果下次登入時，會判斷期限是否超過，如果超過會告知使用者需要驗證
    # 並重新產生 activation_key 與時間
    # TODO : MemberAccount 新增資料時的產生後 7天 期限
    # TODO : MemberAccount 登入帳號 query時的驗證時間與修改 (含UUID)
    key_expired = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : MemberAccount 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Memebr_Account'

    def __unicode__(self):
        pass

class UserInfo(models.Model):
    # TOOD : UserInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 真實姓名 ： 不可以沒有填寫，當註冊完帳號後，進入會員頁面需要要求填寫
    name = models.CharField(max_length=45, null=False, blank=False)
    # 大頭照的上傳路徑
    photo_url = models.ImageField(upload_to='upload/user_profile_photo/')
    # 出生日
    birth_year = models.IntegerField(
        max_length=4,
        default=None, blank=False, null=False,
        # TODO : UserInfo 出生年選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1910, int(datetime.now().year) + 1)]
    )
    birth_month = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=False,
        # TODO : UserInfo 出生月選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 13)]
    )
    birth_day = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=False,
        # TODO : UserInfo 出生日選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 32)]
    )
    # 如果要連結到Radio, 指定布林值對應的選擇，如果預設是不選，則設定default = None
    gender = models.BooleanField(
        default=None,
        null=False,
        # TODO : UserInfo 不設定choice 此部分交由Model Form 處理
        # choices=((True, '男性'), (False, '女性'))
    )
    fk_vocation_type = models.ForeignKey(
        'VocationCategory',
        related_name='users',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 會員帳號註冊
    fk_account = models.OneToOneField('MemberAccount')
    # 使用Facebook註冊
    fk_fb_account = models.OneToOneField('FacebookAccount')

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : UserInfo 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        db_table = 'User_Info'

# 職業種類
class VocationCategory(models.Model):
    type_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO : VocationCategory 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Vocation_Category'

# 付款的方式選擇
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
    # TOOD : CardPayment 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 由於各家卡片長度不一，統一用16(最長)
    card_number = models.CharField(max_length=16)
    # 由於驗證碼長度不一，先使用6碼
    security_code = models.CharField(max_length=6)
    # 外鍵，得知屬於卡個付款紀錄，付款記錄可以得知所有的用卡片付款資料
    fk_payment_record = models.ForeignKey(
        'PaymentRecords',
        related_name='card_payments',
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

# 團體組織的資料，註冊方式不能採用Facebook
class GroupInfo(models.Model):
    # TOOD : GroupInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    # 團體組織圖片的上傳路徑
    photo_url = models.ImageField(upload_to='upload/group_profile_photo/')
    address = models.CharField(max_length=255)
    # 會員帳號註冊
    fk_account = models.OneToOneField('MemberAccount')
    fk_industry = models.ForeignKey(
        'IndustryCategory',
        related_name='groups',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : GroupInfo 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Group_Info'


# 行業產業種類
class IndustryCategory(models.Model):
    type_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO :  IndustryCategory 需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Industry_Category'

# 司機資料
class DriverInfo(models.Model):
    # TOOD : DriverInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 大頭照的上傳路徑
    photo_url = models.ImageField(upload_to='upload/user_profile_photo/')
    # 身分證
    identification_number = models.CharField(max_length=10)
    # 出生日
    birth_year = models.IntegerField(
        max_length=4,
        default=None, blank=False, null=False,
        # TODO : DriverInfo 出生年選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1910, int(datetime.now().year) + 1)]
    )
    birth_month = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=False,
        # TODO : DriverInfo 出生月選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 13)]
    )
    birth_day = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=False,
        # TODO : DriverInfo 出生日選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 32)]
    )
    # 如果要連結到Radio, 指定布林值對應的選擇，如果預設是不選，則設定default = None
    gender = models.BooleanField(
        default=None,
        null=False,
        # TODO : UserInfo 不設定choice 此部分交由Model Form 處理
        # choices=((True, '男性'), (False, '女性'))
    )
    fk_vocation_type = models.ForeignKey(
        'VocationCategory',
        related_name='drivers',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 會員帳號註冊
    fk_account = models.OneToOneField('MemberAccount')
    # 使用Facebook註冊
    fk_fb_account = models.OneToOneField('FacebookAccount')

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : DriverInfo 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Driver_Info'

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
        'VehicleLicense',
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
    # TOOD : DrivingLicnese 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 外鍵，屬於哪種駕照類型，以及可以行駛的車種資料，駕照種類關聯，可以取的有多少駕照
    fk_license_category = models.ForeignKey(
        'DrivingLicneseCategory',
        related_name='licenses',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
    # 外鍵，取得司機的關聯資料
    fk_driver = models.ForeignKey(
        'DriverInfo',
        related_name='vehicles',
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
# TODO ：需後台建檔資料
class DrivingLicneseCategory(models.Model):
    # 類型名稱
    type_name = models.CharField(max_length=45)
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