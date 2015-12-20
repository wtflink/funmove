# -*- coding: utf-8 -*-

from django.db import models

class backendImage(models.Model):
	image = models.FileField(upload_to='imguploadtest/')
	
	class Meta:
		db_table = 'back_Img'

	def delete(self, *args, **kwargs):
		storage, path = self.image.storage, self.image.path
		super(backendImage, self).delete(*args, **kwargs)
		storage.delete(path)