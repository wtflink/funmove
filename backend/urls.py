from django.conf.urls import patterns, url

urlpatterns = patterns(
	'',
	url(r'^$', 'backend.views.index', name='backend_index'),
	url(r'^index/$', 'backend.views.index', name='backend_index')
	
)