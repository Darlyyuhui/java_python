"""Flowers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap

from flower.models import User_Info

sitemaps = {
    'blog': GenericSitemap({'queryset': User_Info.objects.all(), 'date_field': 'pub_date'}, priority=0.6),
    'news':GenericSitemap({'queryset': User_Info.objects.all(),'update_time':'pub_date'},priority = 0.6),
    # 如果还要加其它的可以模仿上面的
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]