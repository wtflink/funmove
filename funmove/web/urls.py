from django.conf.urls import patterns, url

urlpatterns = patterns(
	'',
	url(r'^$', 'web.views.index', name='web_index'),
	url(r'^index/$', 'web.views.index', name='web_index')
)