from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from api.models import (
    UserGameModuleModel, GameModuleModel, UserGameLevelModel, GameLevelModel,
)


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'front/index.html'
    queryset = UserGameModuleModel.objects.filter(game_module__status=GameModuleModel.STATUS.ACTIVE)


class ModuleView(LoginRequiredMixin, DetailView):
    template_name = 'front/module.html'
    pk_url_kwarg = 'module_pk'
    queryset = UserGameModuleModel.objects.filter(game_module__status=GameModuleModel.STATUS.ACTIVE)


class GameView(LoginRequiredMixin, DetailView):
    template_name = 'front/game.html'
    pk_url_kwarg = 'game_pk'
    queryset = UserGameLevelModel.objects.filter(game_level__status=GameLevelModel.STATUS.ACTIVE)
