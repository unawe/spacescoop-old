# from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.timezone import datetime
from spacescoops.models import Article, Category


def home(request):
    return render(request, 'spacescoop/home.html', {
        'featured': Article.add_prefetch_related(Article.objects.featured().exclude(published=False).exclude(release_date__gte=datetime.today()).active_translations())[:4],
        'categories': Category.objects.all(),
    })
