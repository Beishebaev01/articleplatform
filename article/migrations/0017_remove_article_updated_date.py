# Generated by Django 5.0.4 on 2024-05-09 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_article_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_date',
        ),
    ]
