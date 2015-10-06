# -*- coding: utf-8 -*-
from django.db import models

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
