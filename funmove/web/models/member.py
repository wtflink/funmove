# -*- coding: utf-8 -*-
from django.db import models
from facebook_account import FacebookAccount
from uuidfield import UUIDField



# 本網站 帳號登入
class MemberAccount(models.Model):
    # TODO : MemberAccount 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 可以使用 account 或是email 作為登入識別
    account = models.CharField(unique=True, max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    # 電話號碼
    cell_phone = models.CharField(max_length=11, null=False, blank=False)
    # 外鍵，關聯到 MemberType，可以知道屬於哪種MemberType
    # 透過related_name使得MemberType可以得知屬於此Type的MemebrAccount數量
    # 預設related_name會是類別名稱後面補上__set，因此建議有給名稱會比較好辨認
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


# TODO : MemebrType 資料後台建置
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


class UserInfo(models.Model):
    # TODO : UserInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
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
# TODO : VocationCategory 資料後台建置
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

# 團體組織的資料，註冊方式不能採用Facebook
class GroupInfo(models.Model):
    # TODO : GroupInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
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
# TODO : IndustryCategory 資料後台建置
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
    # TODO : DriverInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
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
    # OneToOneField 的預設related_name會是類別的lowercase名稱
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
