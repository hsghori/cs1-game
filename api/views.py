from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated, BasePermission
from api import models
from solution.solution import SOLUTIONS
from api.serializers import CheckGameInputSerializer


class IsOwnProfile(IsAuthenticated):

    def has_permission(self, request, view):
        has_permission = super().has_permission(request, view)
        if not has_permission:
            return False

        pk = view.kwargs.get('pk')
        user_game = models.UserGameLevelModel.objects.get(id=pk)
        return request.user.id == user_game.user_id


class CheckGameLevelViewSet(ViewSet):
    permission_classes = [IsOwnProfile]

    def retrieve(self, request, pk=None):
        raise MethodNotAllowed

    def post(self, request, pk=None):
        serializer = CheckGameInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_game = models.UserGameLevelModel.objects.get(id=pk)

        func = CheckGameLevelViewSet.get_solution_function(user_game)
        for inputArr, outputArr in zip(serializer.validated_data['inputs'], serializer.validated_data['outputs']):
            if func(inputArr) != outputArr:
                break
        else:  # all inputs have passed
            try:
                user_game.mark_complete()
                next_game = user_game.next_game
            except models.NoMoreEntitiesException:
                next_game = None
            return Response({
                'passed': True,
                'next_game': next_game
            })

        return Response({'passed': False, 'next_game': None})

    @staticmethod
    def get_solution_function(user_game):
        return SOLUTIONS[user_game.game_level.external_id]
