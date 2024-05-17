"""
urls.py - Это файл URL-адресов Django, который содержит все URL-адреса проекта.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from article.views import (main_view, article_detail_view, create_article_view, article_update_view,
                           category_article_view, article_delete_view, categories_view)
from user.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', main_view, name='main'),
    path('articles/<int:article_id>/', article_detail_view, name='article_detail'),
    path('create/', create_article_view, name='create_article'),
    path('articles/<int:article_id>/edit/', article_update_view, name='edit_article'),
    path('articles/<int:article_id>/delete/', article_delete_view, name='delete_article'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:categories_id>/', category_article_view, name='category_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

