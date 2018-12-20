"""cloudping URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.cache import cache_page

from apps.ping.views import IndexView, CompanyView

CACHE_TIMEOUT = 60 * 60 * 24
#CACHE_TIMEOUT = 1

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', cache_page(CACHE_TIMEOUT)(IndexView.as_view()), name='index'),
    url(r'^(?P<code>[\w|-]+)/$', cache_page(CACHE_TIMEOUT)(CompanyView.as_view()), name='company'),
    prefix_default_language=False,
)
