# -*- coding: utf-8 -*-

from django.db import models

class backendImage(models.Model):
    image = models.FileField(upload_to='imguploadtest/')
    class Meta:
        db_table = 'Back_Img'