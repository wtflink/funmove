# -*- coding: utf-8 -*-
from django.db import models

class BackAdmin(models.Model):
    # TOOD : BackAdmin 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    account = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # TODO : BackAdmin 建立與更新，需要調整此部分的 新增與修改判斷
    create_admin = models.CharField(max_length=45, null=False)
    update_admin = models.CharField(max_length=45, null=False)
    deactivated_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Back_Admin'

    def __unicode__(self):
        pass
