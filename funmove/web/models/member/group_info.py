# -*- coding: utf-8 -*-
from django.db import models
from member_account import MemberAccount
from industry_category import IndustryCategory


# 團體組織的資料，註冊方式不能採用Facebook
class GroupInfo(models.Model):
    # TODO : GroupInfo 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    # 團體組織圖片的上傳路徑
    photo_url = models.ImageField(upload_to='upload/group_profile_photo/', null=True)
    address = models.CharField(max_length=255)

    # 會員帳號註冊
    fk_account = models.OneToOneField(
        'MemberAccount',
        null=True,
        # 不被 CASCADE 影響，變成NULL 如果有設定NULL
        on_delete=models.SET_NULL
    )
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

