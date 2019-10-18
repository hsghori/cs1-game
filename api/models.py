from django.db import models


class GameModuleModel(models.Model):
    STATUSES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUSES)


class GameLevelModel(models.Model):
    STATUSES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    module = models.ForeignKey(GameModuleModel, related_name='games', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES)
