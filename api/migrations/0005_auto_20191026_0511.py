# Generated by Django 2.2.6 on 2019-10-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191024_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergamelevelmodel',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]