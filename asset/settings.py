#!/usr/bin/env python
#coding:utf-8

from django.conf import settings

import os
settings.TEMPLATES[0]['DIRS'] = [os.path.join(settings.BASE_DIR, 'asset/templates')]

settings.STATICFILES_DIRS =[ os.path.join(settings.BASE_DIR, 'asset/statics')]

settings.TEMPLATES[0]['DIRS'] = [os.path.join(settings.BASE_DIR, 'web/templates')]

settings.STATICFILES_DIRS =[ os.path.join(settings.BASE_DIR, 'web/statics')]
