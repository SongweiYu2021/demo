# Generated by Django 4.0.2 on 2022-03-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameid',
            field=models.IntegerField(unique=True),
        ),
    ]
