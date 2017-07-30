#!/usr/bin/env python
#coding:utf-8


from kingadmin.admin_base import BaseKingAdmin,site
from repository import  models

class AssetAdmin(BaseKingAdmin):
    list_display = ('id','device_type_id','device_status_id','cabinet_num','idc','business_unit',)
    search_fields = ['idc','business_unit','tag','cabinet_num']
    list_per_page = 10
    list_filter = ('idc','business_unit','tag',)

    # dynamic_fk = 'idc',
    actions = ['delete_selected_rows']


site.register(models.Asset,AssetAdmin)
site.register(models.Server)
site.register(models.NetworkDevice)

site.register(models.UserProfile)
site.register(models.UserGroup)

site.register(models.BusinessUnit)
site.register(models.IDC)
site.register(models.Tag)
site.register(models.Disk)
site.register(models.Memory)
site.register(models.NIC)
site.register(models.AssetRecord)
site.register(models.ErrorLog)
site.register(models.ArticleDetail)


