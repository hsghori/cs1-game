from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from api.models import GameModuleModel


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'front/index.html'

    def get_queryset(self):
        return GameModuleModel.objects.filter(status='A')
