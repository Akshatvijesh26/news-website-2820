from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    articles = Article.objects.order_by('-published_at')
    categories = Category.objects.all()
    return render(request, 'myapp/home.html', {
        'articles': articles,
        'categories': categories
    })

def category_articles(request, category_id):
    articles = Article.objects.filter(category_id=category_id).order_by('-published_at')
    categories = Category.objects.all()
    return render(request, 'myapp/home.html', {
        'articles': articles,
        'categories': categories
    })
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    categories = Category.objects.all()
    return render(request, 'myapp/article_detail.html', {
        'article': article,
        'categories': categories
    })