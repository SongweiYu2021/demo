# Generated by Django 4.0.2 on 2022-03-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_sex'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['c_time'], 'verbose_name': 'User', 'verbose_name_plural': 'User'},
        ),
    ]
