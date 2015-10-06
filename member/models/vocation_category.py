# -*- coding: utf-8 -*-
from django.db import models

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
