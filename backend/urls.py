# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
	url(r'^$', 'backend.views.login', name='backend_login'),
	url(r'^index/$', 'backend.views.index', name='backend_index'),
	url(r'^accounts/login/$', 'backend.views.login', name='backend_login'),
	url(r'^accounts/logout/$','backend.views.logout', name='backend_logout'), 
	url(r'^accounts/register/$','backend.views.register', name = 'backend_reg'),
	url(r'^upload/$', 'backend.views.imgUpload', name='backend_imgupload'),
	url(r'^upload/delete/$', 'backend.views.imgShow', name='backend_show'),
	url(r'^upload/delete/(?P<pk>\d+)/$', 'backend.views.imgDel', name='backend_imgdel'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)