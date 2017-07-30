#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import url,include


from cmdb import views

urlpatterns = [
    url(r'asset.html$',views.asset),
     url(r'index/$',views.index,name="dashboard_index"),

]


