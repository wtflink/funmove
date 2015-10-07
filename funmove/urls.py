from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
	'',
	url(r'^$', 'funmove.views.home', name='home'),
	url(r'^web/', include('web.urls')),
	# url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^backend/', include('backend.urls'))
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
