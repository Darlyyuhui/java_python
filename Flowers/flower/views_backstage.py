# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/28
@TODO:
'''
import json
import platform
import time
from logging import exception

import django
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from flower.models import User_Info
from simple.tools import cfg
from simple.tools import commons


def index(request):
    # 如果已登录就直接跳到管理界面
    if request.session.get("sess_admin", False):
        return HttpResponse("admin")

    return commons.render_template(request, "admin/index.html")

def get_code(request):
    ca = commons.Captcha(request)
    # ca.words = ['hello', 'world', 'helloworld']
    ca.type = 'number'  # or word
    ca.img_width = 150
    ca.img_height = 30
    return ca.display()


def login(request):
    imgcode = request.GET.get("code")
    print(imgcode)
    if not imgcode or imgcode == "":
        return commons.res_fail(1, "验证码不能为空")

    ca = commons.Captcha(request)
    if ca.check(imgcode):

        name = request.GET.get("name")
        pwd = request.GET.get("pwd")

        try:

            admin = User_Info.objects.get(name=name, Pass=pwd)
            admin_jsonstr = admin.toJSON()
            admin = json.loads(admin_jsonstr)
            # 删除密码字段
            request.session["sess_admin"] = admin
            return commons.res_success("登录成功")
        except exception as ex:
            print(ex)
            return commons.res_fail(1, "用户或密码不正确")

    else:
        return commons.res_fail(1, "验证码不正确")


def logout(request):
    # 需要登录才可以访问
    if not request.session.get("sess_admin", False):
        return commons.res_fail(1, "需要登录才可以访问")

    del request.session["sess_admin"]
    return commons.res_success("退出登录")