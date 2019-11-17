import random
from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class NoMoreEntitiesException(Exception):
    pass


class GameModuleModel(models.Model):
    STATUS = Choices(
        ('A', 'ACTIVE', 'ACTIVE'),
        ('I', 'INACTIVE', 'INACTIVE')
    )
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    module_number = models.IntegerField(unique=True)
    status = models.CharField(max_length=1, choices=STATUS)


class GameLevelModel(models.Model):
    STATUS = Choices(
        ('A', 'ACTIVE', 'ACTIVE'),
        ('I', 'INACTIVE', 'INACTIVE')
    )
    INPUT_TYPES = Choices(
        ('none', 'NONE', 'None'),
        ('int', 'INTEGER', 'Integer'),
        ('pos_int', 'POSITIVE_INTEGER', 'Positive integer'),
        ('neg_int', 'NEGATIVE_INTEGER', 'Negative integer'),
        ('list_int', 'LIST_INTEGER', 'List integer'),
        ('list_pos_int', 'LIST_POSITIVE_INTEGER', 'List positive integer'),
        ('list_neg_int', 'LIST_NEGATIVE_INTEGER', 'List negative integer'),
    )
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    prompt = models.TextField(max_length=2000)
    blocks = models.TextField(max_length=2000)
    inputs = models.CharField(max_length=128)
    num_inputs = models.IntegerField(default=0)
    list_input_site = models.IntegerField(default=0)
    module = models.ForeignKey(GameModuleModel, related_name='games', on_delete=models.CASCADE)
    level_number = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['level_number', 'module'], name='unique_level_in_module')
        ]

    def get_random_input_values(self):
        def _get_neg_ints(num):
            return [random.randint(-100, 0) for _ in range(num)]

        def _get_pos_ints(num):
            return [random.randint(0, 100) for _ in range(num)]

        def _get_ints(num):
            num_pos = int(num / 2)
            num_neg = int(num / 2)

            if num % 2 != 0:
                increment_neg = random.randint(0, 1)
                if increment_neg:
                    num_neg += 1
                else:
                    num_pos += 1

            assert num_pos + num_neg == num, f'{num_pos}, {num_neg}, {num}'
            nums = _get_pos_ints(num_pos) + _get_neg_ints(num_neg)
            random.shuffle(nums)
            return nums

        if self.inputs == self.INPUT_TYPES.NONE:
            return []
        elif self.inputs == self.INPUT_TYPES.INTEGER:
            return _get_ints(self.num_inputs)
        elif self.inputs == self.INPUT_TYPES.POSITIVE_INTEGER:
            return _get_pos_ints(self.num_inputs)
        elif self.inputs == self.INPUT_TYPES.NEGATIVE_INTEGER:
            return _get_neg_ints(self.num_inputs)
        elif self.inputs == self.INPUT_TYPES.LIST_INTEGER:
            return [
                _get_ints(self.list_input_site) for _ in range(self.num_inputs)
            ]
        elif self.inputs == self.INPUT_TYPES.LIST_POSITIVE_INTEGER:
            return [
                _get_pos_ints(self.list_input_site) for _ in range(self.num_inputs)
            ]
        elif self.inputs == self.INPUT_TYPES.LIST_NEGATIVE_INTEGER:
            return [
                _get_neg_ints(self.list_input_site) for _ in range(self.num_inputs)
            ]


class UserGameModuleModel(models.Model):
    STATUS = Choices(
        ('L', 'LOCKED', 'LOCKED'),
        ('I', 'INCOMPLETE', 'INCOMPLETE'),
        ('C', 'COMPLETE', 'COMPLETE')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_modules', on_delete=models.CASCADE)
    game_module = models.ForeignKey(GameModuleModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        ordering = ['game_module__module_number']
        constraints = [
            models.UniqueConstraint(fields=['user', 'game_module'], name='unique_user_module'),
        ]

    @property
    def is_complete(self):
        return self.status == self.STATUS.COMPLETE

    @property
    def is_locked(self):
        return self.status == self.STATUS.LOCKED

    def mark_complete(self):
        """
        Marks this module as complete
        :raises: NoMoreEntitiesException if there are no more modules
        """
        if self.status == self.STATUS.COMPLETE:
            return

        self.status = self.STATUS.COMPLETE
        self.save()
        self.unlock_next_module()

    def unlock_next_module(self):
        """
        Unlocks the next module in the sequence - additionally unlocks the first game
        in the module.
        :raises: NoMoreEntitiesException if there are no more modules
        """
        remaining_modules = UserGameModuleModel.objects.filter(
            user=self.user,
            game_module__module_number__gt=self.game_module.module_number
        )
        if not remaining_modules:
            raise NoMoreEntitiesException()
        next_module = remaining_modules.first()
        next_module.status = UserGameModuleModel.STATUS.INCOMPLETE
        first_game = next_module.user_games.filter(user=self.user).first()
        first_game.status = UserGameLevelModel.STATUS.INCOMPLETE
        first_game.save()
        next_module.save()


class UserGameLevelModel(models.Model):
    STATUS = Choices(
        ('L', 'LOCKED', 'LOCKED'),
        ('I', 'INCOMPLETE', 'INCOMPLETE'),
        ('C', 'COMPLETE', 'COMPLETE')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_level = models.ForeignKey(GameLevelModel, on_delete=models.CASCADE)
    user_game_module = models.ForeignKey(UserGameModuleModel, related_name='user_games', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['game_level__level_number', 'user_game_module']
        constraints = [
            models.UniqueConstraint(fields=['user', 'game_level'], name='unique_user_level'),
        ]

    @property
    def is_complete(self):
        return self.status == self.STATUS.COMPLETE

    @property
    def is_locked(self):
        return self.status == self.STATUS.LOCKED

    def mark_complete(self):
        """
        Marks this game as complete and unlocks the next game (or module)
        :raises: NoMoreEntitiesException if this is the last game in the last module
        """
        if self.status == self.STATUS.COMPLETE:
            return

        self.status = self.STATUS.COMPLETE
        self.save()
        try:
            self.unlock_next_game()
        except NoMoreEntitiesException:
            self.user_game_module.mark_complete()

    def unlock_next_game(self):
        """
        Unlocks the next game in the module
        :raises: NoMoreEntitiesException if there are no more games in the module
        """
        remaining_games = UserGameLevelModel.objects.filter(
            user=self.user,
            game_level__level_number__gt=self.game_level.level_number,
        )
        if not remaining_games:
            raise NoMoreEntitiesException()
        next_game = remaining_games.first()
        next_game.status = UserGameLevelModel.STATUS.INCOMPLETE
        next_game.save()

    @property
    def next_game(self):
        remaining_games = UserGameLevelModel.objects.filter(
            user=self.user,
            game_level__level_number__gt=self.game_level.level_number,
        )
        if remaining_games:
            return remaining_games.first().id

        remaining_modules = UserGameModuleModel.objects.filter(
            user=self.user,
            game_module__module_number__gt=self.user_game_module.game_module.module_number
        )
        if not remaining_modules:
            return None
        next_module = remaining_modules.first()
        first_game = next_module.user_games.filter(user=self.user).first()
        return first_game.id


@receiver(post_save, sender=User)
def create_user_game_data(sender, instance, created, **kwargs):
    """
    When a user is created, allocates all game modules and game levels to the user. .
    The first module (and the first game in the module) are automatically unlocked.
    """
    if not created:
        return

    for module in GameModuleModel.objects.all():
        user_module = UserGameModuleModel.objects.create(
            user=instance,
            game_module=module,
            status=UserGameModuleModel.STATUS.LOCKED
        )
        for game in module.games.all():
            UserGameLevelModel.objects.create(
                user=instance,
                game_level=game,
                user_game_module=user_module,
                status=UserGameLevelModel.STATUS.LOCKED,
                score=0
            )
    # unlock the first module and the first game of the first module
    first_module = UserGameModuleModel.objects.filter(user=instance).first()
    first_module.status = UserGameModuleModel.STATUS.INCOMPLETE
    first_game = first_module.user_games.first()
    first_game.status = UserGameLevelModel.STATUS.INCOMPLETE
    first_game.save()
    first_module.save()


@receiver(post_save, sender=GameModuleModel)
def create_user_game_module(sender, instance, created, **kwargs):
    """
    When a GameModule is created, allocates the game module to all users.
    The UserGameModule is by default locked.
    """
    if not created:
        return

    for user in User.objects.all():
        UserGameModuleModel.objects.create(
            user=user,
            game_module=instance,
            status=UserGameModuleModel.STATUS.LOCKED
        )


@receiver(post_save, sender=GameLevelModel)
def create_user_game_level(sender, instance, created, **kwargs):
    """
    When a GameLevel is created allocate it to all users.
    The UserGameLevel is by default locked.
    """
    if not created:
        return

    for user in User.objects.all():
        try:
            user_game_module = UserGameModuleModel.objects.get(
                user=user,
                game_module_id=instance.module.id
            )
        except UserGameModuleModel.DoesNotExist:
            user_game_module = UserGameModuleModel.objects.create(
                user=user,
                game_module=instance.module,
                status=UserGameModuleModel.STATUS.LOCKED,
            )
        UserGameLevelModel.objects.create(
            user=user,
            game_level=instance,
            user_game_module=user_game_module,
            status=UserGameLevelModel.STATUS.LOCKED,
        )
