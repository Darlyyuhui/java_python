from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User_Info(models.Model):
    '''
    以下是此对象的属性
    '''
    name = models.CharField(u'用户姓名',max_length=255,default="")
    Pass = models.CharField(u'用户密码',max_length=255,default="")
    sim = models.CharField(u'用户手机',max_length=255,default="")
    icon = models.CharField(u'用户图像',max_length=255,default="")
    idcard = models.CharField(u'用户身份证',max_length=255,default="")
    money = models.CharField(u'金钱',max_length=255,default="")
    same = models.CharField(u'是否一致',max_length=255,default="")
    sex = models.CharField(u'性别',max_length=255,default="")
    tel = models.CharField(u'用户账户',max_length=255,default="")
    token = models.CharField(u'秘钥',max_length=255,default="")
    login = models.CharField(u'登录',max_length=255,default="")
    certificate = models.CharField(u'副参',max_length=255,default="")
    section = models.CharField(u'副参',max_length=255,default="")
    title = models.CharField(u'说明',max_length=255,default="")
    createdate = models.CharField(u'注册日期',max_length=255,default="")


    class Meta:
        verbose_name = '用户分组'
        verbose_name_plural = '用户信息'


