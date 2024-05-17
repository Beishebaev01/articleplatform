# Generated by Django 5.0.4 on 2024-05-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_tag_article_comment_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.tag'),
        ),
    ]
