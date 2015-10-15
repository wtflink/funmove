from django.conf.urls import patterns, url

urlpatterns = patterns(
	'',
	url(r'^$', 'backend.views.login', name='backend_login'),
	url(r'^index/$', 'backend.views.index', name='backend_index'),
	url(r'^accounts/login/$', 'backend.views.login', name='backend_login'),
	url(r'^accounts/logout/$','backend.views.logout', name='backend_logout'), 
	url(r'^accounts/register/$', 'backend.views.register', name='backend_reg'),
)