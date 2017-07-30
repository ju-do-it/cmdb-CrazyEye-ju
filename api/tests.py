from django.test import TestCase

# Create your tests here.

from datetime import  datetime
from repository import models
import json
class DateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.__str__()

    return json.JSONEncoder.default(self, obj)

json_1 = {'num':1112, 'date':datetime.now()}
print (json.dumps(json_1, cls=DateEncoder))


new_assets = models.NewAssetApprovalZone.objects.all()
new_asset_list = []
new_asset_dict = {}

for new_asset in new_assets:
    # new_asset_dict['new_asset_id'] = new_asset.id
    # new_asset_dict['new_asset_sn'] =  new_asset.sn
    # new_asset_dict['new_asset_type'] = new_asset.asset_type
    # new_asset_dict['new_asset_manufactory'] = new_asset.manufactory
    # new_asset_dict['new_asset_model'] = new_asset.model
    #
    # new_asset_dict['new_asset_ram_size'] = new_asset.ram_size
    # new_asset_dict['new_asset_cpu_model'] = new_asset.cpu_model
    # new_asset_dict['new_asset_cpu_count'] =  new_asset.cpu_count
    #
    # new_asset_dict['new_asset_cpu_core_count'] = new_asset.cpu_core_count
    new_asset_dict['new_asset_date'] = new_asset.date

    new_asset_dict = json.dumps(new_asset_dict,cls=DateEncoder)
    print(new_asset_dict)
    # new_asset_list.append(new_asset_dict)
    #
    # print('==new_asset_list==',new_asset_list)