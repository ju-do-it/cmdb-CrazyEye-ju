
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.db import transaction

from web.service import asset,password
from repository import models
from web.service import forms
from web.forms.article  import ArticleForm

class PasswordListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'password_list.html')

class PasswordJsonView(View):
    def get(self, request):
        obj = password.Password()
        response = obj.fetch_assets(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = asset.Asset.delete_assets(request)
        return JsonResponse(response.__dict__)

    def put(self, request):
        response = asset.Asset.put_assets(request)
        return JsonResponse(response.__dict__)


class PasswordDetailView(View):
    def get(self, request, device_type_id, asset_nid):
        response = asset.Asset.assets_detail(device_type_id, asset_nid)
        return render(request, 'asset_detail.html', {'response': response, 'device_type_id': device_type_id})

class PasswordEditlView(View):
    def get(self, request, device_type_id, asset_nid):
        obj = asset.Asset.assets_edit_get(device_type_id, asset_nid)

        return render(request, 'asset_edit.html', {'obj': obj})

    def post(self, request, device_type_id, asset_nid):
        ret = asset.Asset.assets_edit_post(request, device_type_id,  asset_nid)
        return redirect('/asset.html')

class AddPasswordView(View):
    """添加资产信息"""
    def get(self, request, *args, **kwargs):
        obj = forms.AddAssetForm()
        return render(request, 'asset_add.html', {'obj': obj})

    def post(self, request, *args, **kwargs):
        response = asset.Asset.assets_add(request)
        if response.status:
            return redirect('/asset.html')
        else:
            return render(request, 'asset_add.html', {'obj': response.data})



def  ArticleEditlView(request,device_type_id, asset_id):
    '''
    编辑文章。
    '''
    if request.method == 'GET':
       try:
            response = asset.Asset.article_detail(device_type_id, asset_id)
            if not response:
                return render(request, 'backend_no_article.html')
            init_dict = {
                'nid': response.articledetail.nid,
                'title': response.articledetail.title,                   # 文章标题
                'summary': response.articledetail.summary,               # 文章简介
                'content': response.articledetail.content,               # 文章内容
            }
            form = ArticleForm(data=init_dict)
            return render(request, 'backend_edit_article.html',{'form': form, 'asset_id': asset_id,'device_type_id':device_type_id})

       except  AttributeError:
            print('====添加文章====')
            form = ArticleForm()
            return render(request, 'add_asset_article.html', {'form': form,'asset_id': asset_id,'device_type_id':device_type_id})

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            response = asset.Asset.article_detail(device_type_id, asset_id)
            if not response:
                return render(request, 'backend_no_article.html')
            with transaction.atomic():
                # content = form.cleaned_data.pop('content')  # 取出 content 放到变量里。
                # content = XSSFilter().process(content)      # xss 过滤,防止攻击。
                print('=======form.cleaned_data======',form.cleaned_data)
                # detail_id = models.Asset.objects.get(id=asset_id).articledetail.nid
                detail_id = models.Asset.objects.get(id=asset_id)
                response_article = models.ArticleDetail.objects.filter(article=detail_id)

                if  not response_article:
                    print('======response_article======',response_article)
                    form.cleaned_data['article_id'] = asset_id
                    # cleaned_data = {'article_id':'3', 'content': 'fdfadfadfasf', 'title': 'fadfadfa', 'summary': 'dfdfadfasd'}
                    models.ArticleDetail.objects.filter(article_id=asset_id).update_or_create(**form.cleaned_data)
                    return render(request, 'backend_edit_article.html', {'form': form,'asset_id': asset_id,'device_type_id':device_type_id})
                elif response_article:
                    models.ArticleDetail.objects.filter(article_id=asset_id).update(**form.cleaned_data)
            return render(request, 'backend_edit_article.html',{'form': form, 'asset_id': asset_id,'device_type_id':device_type_id})












