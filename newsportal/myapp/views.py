from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def home(request):
    articles = Article.objects.select_related('category', 'author').all()
    categories = Category.objects.all()

    # Get sorting parameter from URL
    sort_by = request.GET.get('sort', '-published_at')

    # Apply sorting
    if sort_by == 'title':
        articles = articles.order_by('title')
    elif sort_by == '-title':
        articles = articles.order_by('-title')
    elif sort_by == 'author':
        articles = articles.order_by('author__username')
    elif sort_by == '-author':
        articles = articles.order_by('-author__username')
    elif sort_by == 'published_at':
        articles = articles.order_by('published_at')
    else:  # default: -published_at (newest first)
        articles = articles.order_by('-published_at')

    return render(request, 'myapp/home.html', {
        'articles': articles,
        'categories': categories,
    })


def category_articles(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).select_related('category', 'author')
    categories = Category.objects.all()

    # Get sorting parameter
    sort_by = request.GET.get('sort', '-published_at')

    # Apply sorting
    if sort_by == 'title':
        articles = articles.order_by('title')
    elif sort_by == '-title':
        articles = articles.order_by('-title')
    elif sort_by == 'author':
        articles = articles.order_by('author__username')
    elif sort_by == '-author':
        articles = articles.order_by('-author__username')
    elif sort_by == 'published_at':
        articles = articles.order_by('published_at')
    else:
        articles = articles.order_by('-published_at')

    return render(request, 'myapp/home.html', {
        'articles': articles,
        'categories': categories,
        'selected_category': category,
    })


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    categories = Category.objects.all()
    return render(request, 'myapp/article_detail.html', {
        'article': article,
        'categories': categories
    })


def about(request):
    categories = Category.objects.all()
    return render(request, 'myapp/about.html', {
        'categories': categories
    })