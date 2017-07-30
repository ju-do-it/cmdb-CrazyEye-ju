#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import importlib
from django.views import View
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
from utils import auth
from api import config
from repository import models
from api.service import asset


class AssetView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AssetView, self).dispatch(request, *args, **kwargs)

    @method_decorator(auth.api_auth)
    def get(self, request, *args, **kwargs):
        """
        获取今日未更新的资产 - 适用SSH或Salt客户端
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # test = {'user': '用户名', 'pwd': '密码'}
        # result = json.dumps(test,ensure_ascii=True)
        # result = json.dumps(test,ensure_ascii=False)
        # return HttpResponse(result)

        # test = {'user': '用户名', 'pwd': '密码'}
        # result = json.dumps(test,ensure_ascii=True)
        # result = json.dumps(test,ensure_ascii=False)
        # return HttpResponse(result,content_type='application/json')

        # test = {'user': '用户名', 'pwd': '密码'}
        # return JsonResponse(test, json_dumps_params={"ensure_ascii": False})

        response = asset.get_untreated_servers()
        return JsonResponse(response.__dict__)

    @method_decorator(auth.api_auth)
    def post(self, request, *args, **kwargs):
        """
        更新或者添加资产信息
        :param request:
        :param args:
        :param kwargs:
        :return: 1000 成功;1001 接口授权失败;1002 数据库中资产不存在
        """
        server_info = json.loads(request.body.decode('utf-8'))  # 在 request.body 中取出 agent 汇报过来的数据
        # print(type(server_info), server_info)     <class 'str'> {汇报的数据}
        server_info = json.loads(server_info)   # 转为 json 的格式

        hostname = server_info['hostname']

        ret = {'code': 1000, 'message': '[%s]更新完成' % hostname}

        server_obj = models.Server.objects.filter(hostname=hostname).select_related('asset').first()  # 通过hostname 获取数据中的数据
        if not server_obj:  # 判断资产是否存在, 整个流程应该是先在平台添加信息,平台只做数据的更新
            ret['code'] = 1002
            ret['message'] = '[%s]资产不存在' % hostname
            return JsonResponse(ret)

        for k, v in config.PLUGINS_DICT.items():
            module_path, cls_name = v.rsplit('.', 1)
            cls = getattr(importlib.import_module(module_path), cls_name)

            # server_obj 数据库中的对象,   server_info agent汇报过来的数据, None 表示谁修改的这条数据 None 表示是agent 汇报过来的
            response = cls.process(server_obj, server_info, None)
            if not response.status:
                ret['code'] = 1003
                ret['message'] = "[%s]资产更新异常" % hostname

            if hasattr(cls, 'update_last_time'):
                cls.update_last_time(server_obj, None)

        return JsonResponse(ret)

class DateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.__str__()

    return json.JSONEncoder.default(self, obj)

#批准入库的资产。
class new_asset_displsy(View):

    def get(self,request,*args,**kwargs):
         new_assets = models.NewAssetApprovalZone.objects.all()

         new_asset_dict = {}
         row_dict = {}
         row_list = []
         cell_list = []

         for new_asset in new_assets:
            row_dict['new_asset_id'] = new_asset.id
            cell_list.append(new_asset.sn)
            cell_list.append(new_asset.asset_type)
            cell_list.append(new_asset.manufactory)
            cell_list.append(new_asset.model)
            cell_list.append(new_asset.ram_size)
            cell_list.append(new_asset.cpu_model)
            cell_list.append(new_asset.cpu_count)
            cell_list.append(new_asset.cpu_core_count)
            cell_list.append('null')
            cell_list.append('null')

            row_dict['cell'] = cell_list
            # row_dict['cell'] = json.dumps(cell_list, cls=DateEncoder)

            # row_dict = json.dumps(row_dict)
            print(row_dict)

            # row_dict = json.dumps(row_dict, cls=DateEncoder)
            row_list.append(row_dict)
            print('===row_list====',row_list)

            # row_list = json.dumps(row_list)

            row_dict = {}
            cell_list = []



         new_asset_dict['page'] = "1"
         new_asset_dict['total'] = 2
         new_asset_dict['records'] = "13"
         new_asset_dict['rows'] = row_list

         return  HttpResponse(json.dumps(new_asset_dict,cls=DateEncoder))







