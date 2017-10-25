# from django.http import HttpResponse, Http404
from django.shortcuts import render
from spacescoops.models import Article, Category


def home(request):
    try:
        articles = Article.objects.featured().active_translations()
        featured = Article.add_prefetch_related(articles)[:4]
    except:
        articles = Article.objects.none()
        featured = []

    try:
        categories = Category.objects.all()
    except:
        categories = Category.objects.none()
    return render(request, 'spacescoop/home.html', {
        'featured': featured,
        'categories': categories,
    })
