from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('account.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('front.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^badges/', include('pinax.badges.urls', namespace='pinax_badges')),
]

urlpatterns += staticfiles_urlpatterns()
