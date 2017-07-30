#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include,url
from asset import  views

urlpatterns = [
    url(r'report/$',views.asset_report, name='asset_report'),
    url(r'report/asset_with_no_asset_id/$',views.asset_with_no_asset_id, name='acquire_asset_id'),

    url(r'^new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),
    url(r'^new_assets/display/$', views.new_asset_display, name="new_assets_display"),

]

#例如 hostsnow_01 中的 url(r'^asset/',include(asset_urls)),

