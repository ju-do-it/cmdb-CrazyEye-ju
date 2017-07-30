from django.test import TestCase

# Create your tests here.

import  requests

response = requests.get('http://www.autohome.com.cn/news')
print(response.content)  #打印出字节的形式

response.encoding = 'gbk'
html = response.text #字符串形式

#字符串结构化成为特殊的数据结构

from bs4 import BeautifulSoup
obj = BeautifulSoup(html,'html.parser')

#找到符合条件的第一个标签
tag = obj.find(name='div',id='auto-channel-lazyload-article')
print("====tag===",tag)

#虽然是列表类型，但是里面包含的是对象【标签对象，标签对象，标签对象】
li_list = tag.find_all(name='li')

for item in li_list:
    h3_obj = item.find(name='h3')
    p_obj = item.find(name='p')
    a_obj = item.find(name='a')

    if h3_obj:
        print(h3_obj.text)  # 打印出对象的内容
        print(p_obj.text)   #
        print(a_obj.attrs.get('href'))
