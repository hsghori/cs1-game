from django.test import TestCase
from api import models
from django.contrib.auth.models import User


class TestUserGameModule(TestCase):

    def setUp(self):
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
            status='A'
        )
        self.game_12 = models.GameLevelModel.objects.create(
            external_id='fake_12',
            title='fake_12',
            description='fake_12',
            module=self.module_1,
            level_number=1,
            status='A'
        )
        self.module_2 = models.GameModuleModel.objects.create(
            external_id='fake_2',
            title='fake_2',
            description='fake_2',
            module_number=1,
            status='A'
        )
        self.game_21 = models.GameLevelModel.objects.create(
            external_id='fake_21',
            title='fake_21',
            description='fake_21',
            module=self.module_2,
            level_number=0,
            status='A'
        )
        self.game_22 = models.GameLevelModel.objects.create(
            external_id='fake_22',
            title='fake_22',
            description='fake_22',
            module=self.module_2,
            level_number=1,
            status='A'
        )
        self.user = User.objects.create_user(
            username='test',
            password='smoothunicorn'
        )

    def test_create_on_user_create(self):
        assert len(models.UserGameModuleModel.objects.all()) == 2
        for module in models.UserGameModuleModel.objects.all():
            assert module.user_games.count() == 2

    def test_create_new_module_and_level(self):
        module = models.GameModuleModel.objects.create(
            external_id='fake_3',
            title='fake_3',
            description='fake_3',
            module_number=3,
            status='A'
        )
        user_module = models.UserGameModuleModel.objects.filter(game_module=module, user=self.user).first()
        assert user_module is not None

        level = models.GameLevelModel.objects.create(
            external_id='fake_13',
            title='fake_13',
            description='fake_13',
            module=module,
            level_number=2,
            status='A'
        )
        user_level = models.UserGameLevelModel.objects.filter(game_level=level, user=self.user).first()
        assert user_level is not None

    def test_unlock_next_game(self):
        user_game = models.UserGameLevelModel.objects.get(user=self.user, game_level=self.game_11)
        user_game.mark_complete()
        next_game = models.UserGameLevelModel.objects.filter(game_level__level_number__gt=user_game.game_level.level_number).first()
        assert user_game.status == models.UserGameLevelModel.STATUS.COMPLETE
        assert next_game.status == models.UserGameLevelModel.STATUS.INCOMPLETE

    def test_unlock_next_module(self):
        user_module = models.UserGameModuleModel.objects.get(user=self.user, game_module=self.module_1)
        user_module.mark_complete()
        next_module = models.UserGameModuleModel.objects.filter(game_module__module_number__gt=user_module.game_module.module_number).first()
        assert user_module.status == models.UserGameModuleModel.STATUS.COMPLETE
        assert next_module.status == models.UserGameModuleModel.STATUS.INCOMPLETE
        assert next_module.user_games.first().status == models.UserGameLevelModel.STATUS.INCOMPLETE

    def test_end_of_module(self):
        user_game = models.UserGameLevelModel.objects.get(user=self.user, game_level=self.game_12)
        user_game.mark_complete()
        next_module = models.UserGameModuleModel.objects.filter(
            game_module__module_number__gt=user_game.user_game_module.game_module.module_number
        ).first()
        assert user_game.user_game_module.status == models.UserGameModuleModel.STATUS.COMPLETE
        assert next_module.status == models.UserGameModuleModel.STATUS.INCOMPLETE
        assert next_module.user_games.first().status == models.UserGameLevelModel.STATUS.INCOMPLETE

    def test_no_more_modules(self):
        user_module = models.UserGameModuleModel.objects.get(user=self.user, game_module=self.module_2)
        self.assertRaises(
            models.NoMoreEntitiesException,
            user_module.mark_complete
        )
        assert user_module.status == models.UserGameModuleModel.STATUS.COMPLETE

    def test_ordering(self):
        # create game levels out of order
        models.GameLevelModel.objects.create(
            external_id='fake_14',
            title='fake_14',
            description='fake_14',
            module=self.module_1,
            level_number=4,
            status='A'
        )
        game_13 = models.GameLevelModel.objects.create(
            external_id='fake_13',
            title='fake_13',
            description='fake_13',
            module=self.module_1,
            level_number=3,
            status='A'
        )
        game = models.UserGameLevelModel.objects.get(user=self.user, game_level=self.game_12)
        game.mark_complete()
        next_game = models.UserGameLevelModel.objects.filter(
            user=self.user,
            game_level__level_number__gt=self.game_12.level_number
        ).first()
        assert next_game.game_level.id == game_13.id
        assert next_game.status == models.UserGameLevelModel.STATUS.INCOMPLETE
