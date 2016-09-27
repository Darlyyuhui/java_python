# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/27
@TODO: 子项目simple的URL合集
'''
from django.conf.urls import url

from simple import views

urlpatterns = [
    url(r'^f/$', views.show,name='show'),
    url(r'^b/$', views.show,name='show'),
]
