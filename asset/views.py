
from django.shortcuts import render,HttpResponse
#from assents import core,models, asset_handle, utils, admin
from asset import core,utils
from repository import models
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from repository import models as cmdb_models

import json


@csrf_exempt
# @utils.token_required

def asset_report(request):       #1. 这个函数处理的是-有 "资产ID"的情况。
    print(request.GET)
    if request.method == 'POST':
        asset_handle = core.Asset(request)
        if asset_handle.data_is_valid():     #数据合法才会被 注册。
            print("------asset data valid:--------")
            asset_handle.data_inject()  # 注射数据到数据库

        return HttpResponse(json.dumps(asset_handle.response))

    return HttpResponse('----test OK ------')

@csrf_exempt
def asset_with_no_asset_id(request): # 2.1、此函数处理没有 "资产ID" 的情况。
    if request.method == 'POST':
        del_handler = core.Asset(request)
        res = del_handler.get_asset_id_by_sn() #2.2、此函数通过 sn 获取 "资产ID"。

        # return render(request,'assets/acquire_asset_id_test.html',{'response':res})
        return HttpResponse(json.dumps(res))

@csrf_exempt
def new_assets_approval(request):

    if request.method == 'POST':
        request.POST = request.POST.copy()  # request.POST 是不能修改的,所以要拷贝一份。
        approved_asset_list = request.POST.getlist('approved_asset_list')
        approved_asset_list = models.NewAssetApprovalZone.objects.filter(id__in=approved_asset_list)

        response_dic = {}
        for obj in approved_asset_list:
            request.POST['asset_data'] = obj.data
            ass_handler = core.Asset(request)

            if ass_handler.data_is_valid_without_id():

                ass_handler.data_inject()
                obj.approved = True
                obj.save()

            response_dic[obj.id] = ass_handler.response

        return render(request, 'new_assets_approval.html',
                      {'new_assets': approved_asset_list, 'response_dic': response_dic})
    else:
        ids = request.GET.get('ids')
        id_list = ids.split(',')
        new_assets = models.NewAssetApprovalZone.objects.filter(id__in=id_list)

        return render(request, 'new_assets_approval.html', {'new_assets': new_assets})

@login_required
def new_asset_display(request):
    if request.method == "GET":

        new_assets = models.NewAssetApprovalZone.objects.all()
        return render(request, 'asset_display_approval.html', {'new_assets': new_assets})

    if request.method == 'POST':
        ids = json.loads(request.POST.get('selected_ids'))
        # ====== selected_ids ==== ['1', '3']

        selected_ids = ','.join(ids)
        print("==== selected_ids ===",selected_ids)
        selected_objs = cmdb_models.NewAssetApprovalZone.objects.filter(id__in=ids)

        if selected_objs:
              print('=== id IN (+ selected_ids +)===','id IN ('+ selected_ids +')')
              # === id IN (+ selected_ids +)=== id IN (1,3)
              #cmdb_models.NewAssetApprovalZone.objects.extra(where=['id IN (' + selected_ids + ')']).delete()

        return render(request, "asset_display_approval.html", locals())


@login_required
def user(request):

    return render(request,'user.html')

# def test(request):
#     if request.method == "GET":
#         new_assets = models.NewAssetApprovalZone.objects.all()
#         return render(request, 'index1.html',{'new_assets': new_assets})