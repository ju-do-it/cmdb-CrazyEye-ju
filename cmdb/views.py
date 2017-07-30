
from django.shortcuts import render
import json
from repository import models as cmdb_models

def asset(request):

    if  "type" in request.GET:
        from cmdb.views_func import asset
        asset_id = request.GET.get('id')

        if request.GET.get('type') == "select":
            result_data = asset.View_details(asset_id)
            return render(request,'cmdb/asset_select.html',locals())

        elif request.GET.get('type') == "edit":  # 编辑 资产
            pass
        elif request.GET.get('type') == 'create':  #创建 资产
            pass
        elif request.GET.get('type') == 'delete':
            pass

        if request.GET.get('type') == "select":
            result_data = asset.View_details(asset_id)
            return render(request,'cmdb/asset_select.html',locals())


    if request.method == 'POST':

        ids = json.loads(request.POST.get('selected_ids'))
        print ('====== selected_ids ====',ids)
        # ====== selected_ids ==== ['1', '3']

        selected_ids = ','.join(ids)
        print("==== selected_ids ===",selected_ids)
        # ==== selected_ids === 1,3

        selected_objs = cmdb_models.Asset.objects.filter(id__in=ids)

        if selected_objs:
              print('=== id IN (+ selected_ids +)===','id IN ('+ selected_ids +')')
              # === id IN (+ selected_ids +)=== id IN (1,3)
              cmdb_models.Asset.objects.extra(where=['id IN (' + selected_ids + ')']).delete()


    cmdb_models_obj = cmdb_models.Asset.objects.all()

    return render(request, "cmdb/asset.html", locals())



def index(request):
    ''' dashboard 控制面板 '''
    return render(request,'layout/index.html',locals())
