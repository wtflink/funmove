# -*- coding: utf-8 -*-
from django.db import models
from facebook_account import FacebookAccount
from member_account import MemberAccount

# 第一版：
# 生日，性別，職業皆可以Null

# 使用者資料
class UserInfo(models.Model):
    # TODO : UserInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # 真實姓名 ： 不可以沒有填寫，當註冊完帳號後，進入會員頁面需要要求填寫
    name = models.CharField(max_length=45, null=False, blank=False)
    # 大頭照的上傳路徑
    photo_url = models.ImageField(upload_to='upload/user_profile_photo/', null=True)
    # 出生日
    birth_year = models.IntegerField(
        max_length=4,
        default=None, blank=False, null=True,
        # TODO : UserInfo 出生年選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1910, int(datetime.now().year) + 1)]
    )
    birth_month = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=True,
        # TODO : UserInfo 出生月選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 13)]
    )
    birth_day = models.IntegerField(
        max_length=2,
        default=None, blank=False, null=True,
        # TODO : UserInfo 出生日選項，要在ModelForm定義
        # choices=[(i, i) for i in range(1, 32)]
    )
    # 如果要連結到Radio, 指定布林值對應的選擇，如果預設是不選，則設定default = None
    gender = models.BooleanField(
        default=None,
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
    fk_account = models.OneToOneField(
        'MemberAccount',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL)
    # 使用Facebook註冊
    fk_fb_account = models.OneToOneField(
        'FacebookAccount',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL)

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
