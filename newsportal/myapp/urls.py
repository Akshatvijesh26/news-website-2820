from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_articles, name='category_articles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('about/', views.about, name='about'),
]