# Generated by Django 2.2.6 on 2019-10-15 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModuleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external_id', models.CharField(max_length=30, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GameLevelModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external_id', models.CharField(max_length=30, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='api.GameModuleModel')),
            ],
        ),
    ]
