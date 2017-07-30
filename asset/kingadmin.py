#!/usr/bin/env python
#coding:utf-8

from kingadmin.admin_base import BaseKingAdmin,site
from repository import  models



site.register(models.NewAssetApprovalZone)
