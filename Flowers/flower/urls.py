# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/27
@TODO: 子项目flower的URL合集
'''
from django.conf.urls import url

from flower import views
from flower import views_backstage

urlpatterns = [
    #后台页面部分
	url(r'^backstage/index$',views_backstage.index,name='flower.views_backstage.index'),
	#验证码
	url(r'^backstage/get_code$', views_backstage.get_code,name='flower.views_backstage.get_code'),
	#后台请求数据部分
	url(r'^backstage/login$',views_backstage.login,name='flower.views_backstage.login'),
	url(r'^backstage/logout$',views_backstage.logout,name='flower.views_backstage.logout'),
]