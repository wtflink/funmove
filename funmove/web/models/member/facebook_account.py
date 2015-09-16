# -*- coding: utf-8 -*-
from django.db import models

# Facebook 帳號登入
class FacebookAccount(models.Model):
    # Field name made lowercase.
    uid = models.BigIntegerField(db_column='UID', primary_key=True)
    token = models.CharField(max_length=255)

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : FacebookAccount 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Facebook_Account'

    def __unicode__(self):
        pass