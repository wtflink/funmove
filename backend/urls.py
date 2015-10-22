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
	url(r'^list/$', 'backend.views.list', name='backend_list'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)