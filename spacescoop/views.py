# from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.timezone import datetime
from spacescoops.models import Article, Category


def home(request):
    return render(request, 'spacescoop/home.html', {
        'featured': Article.add_prefetch_related(Article.objects.available().filter(featured=True))[:4],
        'categories': Category.objects.all(),
    })
