'''
views.py - это файл, который содержит все представления Django.

FBV - это функции представления Django.
CBV - это классы представления Django.

objects - это менеджер модели Django,
который позволяет выполнять запросы к базе данных.

# all() - метод QuerySet, который возвращает все объекты модели.
posts = Post.objects.all() # Получаем QuerySet всех объектов модели Post.
# filter() - метод QuerySet, который возвращает объекты модели, удовлетворяющие условию.
# posts = Post.objects.filter(title__icontains='python')  # Получаем QuerySet объектов модели Post, у которых в поле title содержится 'python'
# exclude() - метод QuerySet, который исключает объекты модели, удовлетворяющие условию.
# posts = Post.objects.exclude(title__icontains='python')  # Получаем QuerySet объектов модели Post, у которых в поле title не содержится 'python'
# order_by() - метод QuerySet, который сортирует объекты модели по указанному полю.
# posts = Post.objects.order_by('created_at')  # Получаем QuerySet объектов модели Post, отсортированных по полю created_at
# reverse() - метод QuerySet, который меняет порядок объектов на обратный.
# posts = Post.objects.reverse()  # Получаем QuerySet объектов модели Post в обратном порядке
# first() - метод QuerySet, который возвращает первый объект модели.
# post = Post.objects.first()  # Получаем первый объект модели Post
# last() - метод QuerySet, который возвращает последний объект модели.
# post = Post.objects.last()  # Получаем последний объект модели Post
# count() - метод QuerySet, который возвращает количество объектов модели.
# count = Post.objects.count()  # Получаем количество объектов модели Post
# exists() - метод QuerySet, который возвращает True, если объекты модели существуют, иначе False.
# exists = Post.objects.exists()  # Проверяем, существуют ли объекты модели Post
# values() - метод QuerySet, который возвращает QuerySet значений указанных полей модели.
# values = Post.objects.values('title', 'created_at')  # Получаем QuerySet значений полей title и created_at модели Post
# values_list() - метод QuerySet, который возвращает QuerySet значений указанных полей модели в виде кортежей.
# values_list = Post.objects.values_list('title', 'created_at')  # Получаем QuerySet значений полей title и created_at модели Post.
# create() - метод QuerySet, который создает новый объект модели.
# post = Post.objects.create(title='New Post', text='New Text')  # Создаем новый объект модели Post
# get() - метод QuerySet, который возвращает один объект модели, удовлетворяющий условию.
# post = Post.objects.get(id=1)  # Получаем объект модели Post с id=1
# update() - метод QuerySet, который обновляет объекты модели, удовлетворяющие условию.
# Post.objects.filter(title__icontains='python').update(title='New Title')  # Обновляем объекты модели Post, у которых в поле title содержится 'python'
# delete() - метод QuerySet, который удаляет объекты модели, удовлетворяющие условию.
# Post.objects.filter(title__icontains='python').delete()  # Удаляем объекты модели Post, у которых в поле title содержится 'python'
Документация Django: https://docs.djangoproject.com/en/4.0/topics/db/queries/

Field lookups - это специальные методы для фильтрации QuerySet по значениям полей модели.
Field lookups:
1. exact - точное совпадение.
2. iexact - точное совпадение без учета регистра.
3. contains - содержит.
4. icontains - содержит без учета регистра.
5. in - входит в список.
6. gt - больше.
7. gte - больше или равно.
8. lt - меньше.
9. lte - меньше или равно.
10. startswith - начинается с.
11. istartswith - начинается с без учета регистра.
12. endswith - заканчивается на.
13. iendswith - заканчивается на без учета регистра.
14. range - в диапазоне.
15. year - год.
16. month - месяц.
17. day - день.
18. week_day - день недели.
19. isnull - равно NULL.
20. regex - регулярное выражение.
21. iregex - регулярное выражение без учета регистра.
Документация: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

Qurey Parameters - это параметры запроса, которые передаются в URL-адресе.
https://exaple.com?name=Esen&age=18&city=Almaty

Paggination:

        # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]
        # limit = 3, page = 1

        # Formula:
        # start = (page - 1) * limit
        # end = page * limit

        # Example 1:
        # page = 1, limit = 3
        # start = (1 - 1) * 3 = 0
        # end = 1 * 3 = 3
        # posts = posts[0:3]
        # Example 2:
        # page = 3, limit = 3
        # start = (3 - 1) * 3 = 6
        # end = 3 * 3 = 9
        # posts = posts[6:9]
'''


from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db.models import Q
from article.models import Article, Category, Comment
from article.forms import ArticleForm, CommentForm


def main_view(request):
    sort = request.GET.get('sort', None)

    if sort == 'А-Я':
        articles = Article.objects.all().order_by('title')
    elif sort == 'Я-А':
        articles = Article.objects.all().order_by('-title')
    else:
        articles = Article.objects.all().order_by('-created_date')

    search = request.GET.get('search')

    if search:
        articles = Article.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )

    page = int(request.GET.get('page', 1))

    limit = 8
    max_page = articles.count() / limit

    if round(max_page) < max_page:
        max_page = round(max_page) + 1
    else:
        max_page = round(max_page)

    start = (page - 1) * limit
    end = page * limit

    articles = articles[start:end]

    context = {'articles': articles, 'sort': sort, 'max_page': range(1, max_page + 1)}
    return render(request, 'article/main.html', context)


def article_detail_view(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse("Article not found", status=404)
    if request.method == "GET":
        context = {
            'article': article
        }
        return render(request, 'article/article_detail.html', context)

    comments = article.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect(f'/articles/{article_id}/')

    else:
        form = CommentForm()

    return render(request, 'article/article_detail.html', {'article': article, 'comments': comments, 'form': form})


def create_article_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article/create_article.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            form.save()
            return redirect("main")

        return render(request, 'article/create_article.html', {'form': form})


def article_update_view(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse("Статья не найдена", status=404)

    if request.method == "GET":
        form = ArticleForm(instance=article)

        context = {'form': form}

        return render(request, "article/article_update.html", context)

    elif request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            form.save()

            return redirect(f'/articles/{article_id}/')

        return render(request, 'article/article_update.html', {'form': form})


def article_delete_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('main')

    return render(request, 'article/article_delete.html', {'article': article})


def category_article_view(request, categories_id):
    sort = request.GET.get('sort', None)

    category = get_object_or_404(Category, id=categories_id)

    if sort == 'А-Я':
        articles = category.articles.all().order_by('title')
    elif sort == 'Я-А':
        articles = category.articles.all().order_by('-title')
    else:
        articles = category.articles.all().order_by('-created_date')

    return render(request, 'article/category_article.html', {'category': category, 'articles': articles, 'sort': sort})


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'article/categories.html', {'categories': categories})