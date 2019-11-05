from django.urls import reverse
import pytest
from .fixtures import logged_in_client, load_game_data, create_user, get_client

class TestGameView:

    def test_list_game_without_login_fails(self, client):
        response = client.get(reverse('game', args=(1,)))
        assert response.status_code == 302

    def test_list_game_succeeds(self, load_game_data, logged_in_client):
        response = logged_in_client.get(reverse('game', args=(1,)))

        assert response.status_code == 200
        assert response.template_name[0] == 'front/game.html'


# class TestModuleView:
#
#     def test_list_game_succeeds(self, load_game_data, logged_in_client):
#         response = logged_in_client.get(reverse('module', args=(1,)))
#
#         assert response.status_code == 200
#         assert response.template_name[0] == 'front/game.html'



