# -*- coding: utf-8 -*-
from django.db import models

class FacebookAccount(models.Model):
    # Field name made lowercase.
    uid = models.BigIntegerField(db_column='UID', primary_key=True)
    token = models.CharField(max_length=255)

    class Meta:
        db_table = 'Facebook_Account'

    def __unicode__(self):
        pass
