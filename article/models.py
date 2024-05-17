'''
models.py - это файл, который содержит все модели Django.

ORM - Object-Relational Mapping - это концепция,
которая позволяет работать с базами данных, используя объекты и методы.
'''
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "Category"


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articles', null=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    title = models.CharField(max_length=155)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='articles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        db_table = 'Article'


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        db_table = "Comment"
