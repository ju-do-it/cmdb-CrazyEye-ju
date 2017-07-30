#!/usr/bin/env python
#coding:utf-8

import requests
from bs4 import BeautifulSoup

# 第一步：获取csrf
r1 = requests.get(url='https://github.com/login')
b1 = BeautifulSoup(r1.text,'html.parser')

tag = b1.find(name='input',attrs={'name':'authenticity_token'})

# print(tag.attrs.get('value')) #等价于tag.get('value')
token = tag.get('value')

#第二步：发送POST请求携带用户名和密码。。。。

 # r2 = requests.post()  #这两也是等价于的。。
 # r2 = requests.request('post',)

r2 = requests.post(
     url='https://github.com/session',
    data={
        'commit':'Sign in',
        'utf8': '✔',
        'authenticity_token': token,
        'login':'root',
        'password':'111qqq,,,',
    }
)

# 差看返回值是否登录成功。
# 1、r2获取状态码
#    r2 获取响应头【location】

# 2、或者根据错误提示
cookies_dict = r2.cookies.get_dict()

# 第三步 访问个人页面，携带cookis
r3  = requests.get(
    url='https://github.com/settings/repositories',
    cookies = cookies_dict
)
print(r3.text)

# 返回值
# <Response [200]>






















