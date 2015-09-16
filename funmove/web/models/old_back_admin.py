# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BackAdmin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    account = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    delete_date = models.DateTimeField(blank=True, null=True)
    deactivated = models.IntegerField()
    create_admin = models.ForeignKey('self')
    update_admin = models.ForeignKey('self')
    deactivated_admin = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Back_Admin'


class FacebookAccount(models.Model):
    uid = models.BigIntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Facebook_Account'
