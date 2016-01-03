from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
	'',
	url(r'^$', 'order.views.order_index', name='order_index'),
	url(r'^index/$', 'order.views.order_index', name='order_index'),
	url(r'^when/$', 'order.views.order', name='order_when'),
	url(r'^confirm/(?P<confirmation_key>\w+)/', 'order.views.confirm', name='order_confirm'),
	url(r'^events.json$', 'order.views.events_json', name='order_events.json'),
	url(r'^success/$', 'order.views.order_success', name='order_success'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)