from django import forms
from article.models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image', 'title', 'content', 'categories']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 10,
                'rows': 3,
                'placeholder': "Введите текст"
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control',
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']