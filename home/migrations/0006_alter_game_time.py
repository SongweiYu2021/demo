# Generated by Django 4.0.2 on 2022-03-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_game_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=None, verbose_name='发布日期'),
        ),
    ]