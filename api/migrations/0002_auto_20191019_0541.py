# Generated by Django 2.2.6 on 2019-10-19 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelevelmodel',
            name='status',
            field=models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE')], max_length=1),
        ),
        migrations.AlterField(
            model_name='gamemodulemodel',
            name='status',
            field=models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE')], max_length=1),
        ),
        migrations.CreateModel(
            name='UserGameModuleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('L', 'LOCKED'), ('I', 'INCOMPLETE'), ('C', 'COMPLETE')], max_length=1)),
                ('game_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GameModuleModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_modules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGameLevelModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('L', 'LOCKED'), ('I', 'INCOMPLETE'), ('C', 'COMPLETE')], max_length=1)),
                ('score', models.IntegerField()),
                ('game_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GameLevelModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_game_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_games', to='api.UserGameModuleModel')),
            ],
        ),
    ]
