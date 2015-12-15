from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
	'',
	url(r'^$', 'order.views.order_index', name='order_index'),
	url(r'^index/$', 'order.views.order_index', name='order_index'),
	url(r'^when/$', 'order.views.order', name='order_when'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)