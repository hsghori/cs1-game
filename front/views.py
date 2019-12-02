from collections import defaultdict
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Count
from api.models import (
    UserGameModuleModel, GameModuleModel, UserGameLevelModel, GameLevelModel,
)
from pinax.badges.models import BadgeAward
from pinax.badges.registry import badges


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'front/index.html'

    def get_queryset(self):
        return UserGameModuleModel.objects.filter(
            user=self.request.user,
            game_module__status=GameModuleModel.STATUS.ACTIVE
        )


class ModuleView(LoginRequiredMixin, DetailView):
    template_name = 'front/module.html'
    pk_url_kwarg = 'module_pk'

    def get_queryset(self):
        return UserGameModuleModel.objects.filter(
            user=self.request.user,
            game_module__status=GameModuleModel.STATUS.ACTIVE
        )


class GameView(LoginRequiredMixin, DetailView):
    template_name = 'front/game.html'
    pk_url_kwarg = 'game_pk'

    def get_queryset(self):
        return UserGameLevelModel.objects.filter(
            user=self.request.user,
            game_level__status=GameLevelModel.STATUS.ACTIVE
        )


class BadgeView(LoginRequiredMixin, ListView):
    template_name = 'front/badges.html'

    def get_queryset(self):
        return BadgeAward.objects.filter(
            user=self.request.user,
        )
