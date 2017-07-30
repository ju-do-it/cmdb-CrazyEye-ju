#!/usr/bin/env python
#coding:utf-8

from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node,TemplateEncodingError

register = template.Library()

@register.simple_tag
def article_message(context):
    if context:
       print('========context=========',context)
       return mark_safe(context)


