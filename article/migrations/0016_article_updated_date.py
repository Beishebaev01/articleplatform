# Generated by Django 5.0.4 on 2024-05-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_rename_tag_category_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
