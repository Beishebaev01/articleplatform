'''
admin.py - это файл, который содержит настройки администратора Django.
'''

from django.contrib import admin
from article.models import Article, Comment, Category

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
