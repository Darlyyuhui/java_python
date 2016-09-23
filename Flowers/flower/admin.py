from django.contrib import admin

# Register your models here.
from flower.models import User_Info


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'Pass', 'sim', 'icon', 'idcard')


admin.site.register(User_Info,UserInfoAdmin)
