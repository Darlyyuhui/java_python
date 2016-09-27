# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/27
@TODO: 子项目flower的URL合集
'''
from django.conf.urls import url

from flower import views

urlpatterns = [
    url(r'^f/index$', views.index,name='index'),
    url(r'^b/$', views.index,name='index'),
]