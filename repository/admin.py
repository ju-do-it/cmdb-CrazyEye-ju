
from django.contrib import admin
from repository import models

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id','device_type_id','device_status_id','cabinet_num','idc','business_unit')
    search_fields = ['sn','idc','business_unit','tag']
    list_per_page = 10
    list_filter = ('idc','business_unit','tag',)

    # actions = ['delete_selects_row_']

    dynamic_fk = 'idc'

class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ('id','title')



admin.site.register(models.Asset,AssetAdmin)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)
admin.site.register(models.AdminInfo)
admin.site.register(models.BusinessUnit)
admin.site.register(models.IDC)
admin.site.register(models.Tag)

admin.site.register(models.AssetRecord)
admin.site.register(models.ErrorLog)
admin.site.register(models.ArticleDetail,ArticleDetailAdmin)
admin.site.register(models.NewAssetApprovalZone)
admin.site.register(models.Manufactory)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.NIC)
admin.site.register(models.Memory)




