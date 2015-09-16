# -*- coding: utf-8 -*-
from django.db import models
from facebook_account import FacebookAccount
from member_account import MemberAccount
from vocation_category import VocationCategory

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
