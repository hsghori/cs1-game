from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(
    r'check-game', views.CheckGameLevelViewSet, base_name='check-game'
)

urlpatterns = [
    path('', include(router.urls)),
]
