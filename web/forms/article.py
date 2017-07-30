#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django import forms as django_forms
from django.forms import fields as django_fields
from django.forms import widgets as django_widgets

from repository import models


class ArticleForm(django_forms.Form):
    title = django_fields.CharField(
        widget=django_widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '文章标题'})
    )
    summary = django_fields.CharField(
        widget=django_widgets.Textarea(attrs={'class': 'form-control', 'placeholder': '文章简介', 'rows': '3'})
    )
    content = django_fields.CharField(
        widget=django_widgets.Textarea(attrs={'class': 'kind-content'})
    )


