# Generated by Django 4.0.2 on 2022-03-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ns_user', '0002_rename_user_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user',
        ),
    ]