
from django.conf.urls import patterns, include, url

from simple import views_admin
from simple import views_site

urlpatterns = [
	#后台页面部分
	url(r'^admin/index$',views_admin.index,name='simple.views_admin.index'),
	url(r'^admin/admin$', views_admin.admin,name='simple.views_admin.admin'),
	#验证码
	url(r'^admin/get_code$', views_admin.get_code,name='simple.views_admin.get_code'),
	#后台请求数据部分
	url(r'^admin/ajax_login$',views_admin.ajax_login,name='simple.views_admin.ajax_login'),
	url(r'^admin/ajax_logout$',views_admin.ajax_logout,name='simple.views_admin.ajax_logout'),
	url(r'^admin/ajax_menu_list$',views_admin.ajax_menu_list,name='simple.views_admin.ajax_menu_list'),
	url(r'^admin/ajax_admin_list$',views_admin.ajax_admin_list,name='simple.views_admin.ajax_admin_list'),
	url(r'^admin/ajax_admin_add$',views_admin.ajax_admin_add,name='simple.views_admin.ajax_admin_add'),
	url(r'^admin/ajax_admin_del$',views_admin.ajax_admin_del,name='simple.views_admin.ajax_admin_del'),
	url(r'^admin/ajax_admin_updatepwd$',views_admin.ajax_admin_updatepwd,name='simple.views_admin.ajax_admin_updatepwd'),
	url(r'^admin/ajax_art_single_get$',views_admin.ajax_art_single_get,name='simple.views_admin.ajax_art_single_get'),
	url(r'^admin/ajax_art_single_update$',views_admin.ajax_art_single_update,name='simple.views_admin.ajax_art_single_update'),
	url(r'^admin/ajax_dataclass_list$',views_admin.ajax_dataclass_list,name='simple.views_admin.ajax_dataclass_list'),
	url(r'^admin/ajax_dataclass_get$',views_admin.ajax_dataclass_get,name='simple.views_admin.ajax_dataclass_get'),
	url(r'^admin/ajax_dataclass_add$',views_admin.ajax_dataclass_add,name='simple.views_admin.ajax_dataclass_add'),
	url(r'^admin/ajax_dataclass_del$',views_admin.ajax_dataclass_del,name='simple.views_admin.ajax_dataclass_del'),
	url(r'^admin/ajax_data_list$',views_admin.ajax_data_list,name='simple.views_admin.ajax_data_list'),
	url(r'^admin/ajax_data_get$',views_admin.ajax_data_get,name='simple.views_admin.ajax_data_get'),
	url(r'^admin/ajax_data_add$',views_admin.ajax_data_add,name='simple.views_admin.ajax_data_add'),
	url(r'^admin/ajax_data_del$',views_admin.ajax_data_del,name='simple.views_admin.ajax_data_del'),
	
	#前台
	url(r'^site/index$',views_site.index,name='simple.views_site.index'),

]
