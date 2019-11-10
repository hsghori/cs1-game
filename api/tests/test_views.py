import json
from unittest import mock
from django.test import TestCase
from django.contrib.auth.models import User
from api import models


class TestCheckGameLevelViewSet(TestCase):

    def setUp(self):
        super().setUp()
        self.module_1 = models.GameModuleModel.objects.create(
            external_id='fake_1',
            title='fake_1',
            description='fake_1',
            module_number=0,
            status='A'
        )
        self.game_11 = models.GameLevelModel.objects.create(
            external_id='fake_11',
            title='fake_11',
            description='fake_11',
            module=self.module_1,
            level_number=0,
            prompt='',
            blocks='',
            status='A'
        )
        self.game_12 = models.GameLevelModel.objects.create(
            external_id='fake_12',
            title='fake_12',
            description='fake_12',
            module=self.module_1,
            prompt='',
            blocks='',
            level_number=1,
            status='A'
        )
        self.user = User.objects.create_user(
            username='test',
            password='smoothunicorn'
        )
        self.user_game_level_id = models.UserGameLevelModel.objects.get(
            game_level_id=self.game_11.id,
            user_id=self.user.id).id
        self.client.force_login(user=self.user)

    @mock.patch('api.views.CheckGameLevelViewSet.get_solution_function', return_value=lambda x: ['Hello world!'])
    def test_post_game_passed(self, mock_solutions):
        url = f'/api/check-game/{self.user_game_level_id}/'
        data = {
            'inputs': [],
            'outputs': ['Hello world!']
        }
        user_level = models.UserGameLevelModel.objects.get(id=self.user_game_level_id)
        next_user_level = models.UserGameLevelModel.objects.get(user_id=self.user.id, game_level__id=self.game_12.id)
        assert not user_level.is_complete
        assert next_user_level.is_locked

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json')

        user_level = models.UserGameLevelModel.objects.get(id=self.user_game_level_id)
        next_user_level = models.UserGameLevelModel.objects.get(user_id=self.user.id, game_level__id=self.game_12.id)
        assert response.status_code == 200
        assert response.data['passed']
        assert user_level.is_complete
        assert not next_user_level.is_locked

    @mock.patch('api.views.CheckGameLevelViewSet.get_solution_function', return_value=lambda x: ['Hello world!'])
    def test_post_game_not_passed(self, mock_solutions):
        url = f'/api/check-game/{self.user_game_level_id}/'
        data = {
            'inputs': [],
            'outputs': ['incorrect']
        }
        next_user_level = models.UserGameLevelModel.objects.get(user_id=self.user.id, game_level__id=self.game_12.id)
        assert next_user_level.is_locked

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 200
        assert not response.data['passed']
        next_user_level = models.UserGameLevelModel.objects.get(user_id=self.user.id, game_level__id=self.game_12.id)
        assert next_user_level.is_locked

    def test_invalid_auth(self):
        url = f'/api/check-game/{self.user_game_level_id}/'
        user = User.objects.create_user(
            username='test2',
            password='smoothunicorn'
        )
        self.client.force_login(user=user)
        response = self.client.post(
            url,
            data=json.dumps({}),
            content_type='application/json')
        assert response.status_code == 403

    def test_bad_request(self):
        url = f'/api/check-game/{self.user_game_level_id}/'
        data = {'outputs': []}
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 400
        assert response.data == {'inputs': ['This field is required.']}

        response = self.client.post(
            url,
            data=json.dumps({}),
            content_type='application/json')
        assert response.status_code == 400
        assert response.data == {
            'inputs': ['This field is required.'],
            'outputs': ['This field is required.'],
        }
