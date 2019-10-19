from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^module/(?P<module_pk>[^/]+)/$', views.ModuleView.as_view(), name="module"),
    url(r'^game/(?P<game_pk>[^/]+)/$', views.GameView.as_view(), name='game'),
    url('^$', views.IndexView.as_view(), name="index"),
]
