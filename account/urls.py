from django.conf.urls import url
from .views import SignUpView

urlpatterns = [
    url(r'create-account/', SignUpView.as_view(), name='signup'),
]