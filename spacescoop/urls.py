"""spacescoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from smartpages.views import SmartPageView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', 'spacescoop.views.home', name='home'),
    url(r'^search/', 'spacescoop.search.views.search', name='search'),
    url(r'^scoops/', include('spacescoop_shared.articles.urls', namespace='articles')),
    url(r'^topics/', include('spacescoop_shared.articles.urls_categories', namespace='categories')),
    url(r'^friends/', include('spacescoop_shared.articles.urls_partners', namespace='partners')),
    url(r'^words/', include('glossary.urls', namespace='glossary')),
    url(r'^newsletter/', include('spacescoop.newsletter.urls', namespace='newsletter')),

    # (r'^images/?$', RedirectView.as_view(url='/scoops/', permanent=True)),
)

if settings.DEBUG:
    # import debug_toolbar
    urlpatterns += patterns('',
        # # test 404 and 500 pages
        (r'^500/$', TemplateView.as_view(template_name='500.html')),
        (r'^404/$', TemplateView.as_view(template_name='404.html')),

        # redirects (use nginx rewrite for production)
        (r'^favicon\.ico/?$', RedirectView.as_view(url='/static/favicons/favicon.ico', permanent=True)),

        # serve MEDIA_ROOT (uploaded files) in development
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

        # # debug_toolbar
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += i18n_patterns(
    url(r'^(?P<url>.*/)$', SmartPageView.as_view(), name='smartpage'),
)
