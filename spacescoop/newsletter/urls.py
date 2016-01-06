from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.ArticleListView.as_view(), name='list'),
    # url(r'^$', 'spacescoop.views.home', name='home'),
    url(r'^subscribe/$', 'spacescoop.newsletter.views.subscribe', name='subscribe'),
]