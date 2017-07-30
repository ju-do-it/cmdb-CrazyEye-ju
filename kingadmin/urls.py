
from django.conf.urls import url,include
from kingadmin import views

urlpatterns = [

    url(r'^login/$', views.acc_login, name="acc_login"),
    url(r'^logout/$', views.acc_logout, name="acc_logout"),

    #修改密码
    url(r'^(\w+)/(\w+)/change/(\d+)/password/$', views.password_reset_form, name='password_reset'),
    url(r'^account/password_reset/$', views.personal_password_reset, name='personal_password_reset'),

    url(r'^$', views.app_index, name="table_index"),                     # 显示--所有【app】和注册的【表】
    url(r'^(\w+)/$', views.app_tables, name="app_tables"),                        # 显示--每个【app】的注册的【表】
    url(r'^(\w+)/(\w+)/$',views.display_table_list, name="table_list"),           # 显示--每个【表】的数据。

    url(r'^(\w+)/(\w+)/add/$', views.table_add, name="table_add"),                # 增加【表】数据。
    url(r'^(\w+)/(\w+)/change/(\d+)/$', views.table_change, name="table_change"), # 修改【表】数据
    url(r'^(\w+)/(\w+)/delete/(\d+)/$', views.table_del, name="table_del"),       # 删除【表】数据

]

