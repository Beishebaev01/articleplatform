# Generated by Django 5.0.4 on 2024-05-16 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
