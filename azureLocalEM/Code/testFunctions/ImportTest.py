import os
import sys
import json 
print(sys.path)

sys.path.append('azureLocalEm/Code/testFunctions/functionActions')
print(sys.path)

import db_test_upload

from db_test_upload import DataInsert
filepath = 'azureLocalEm/Data/jsonEXAMPLE2.json'
with open(filepath, 'r') as f:
    json_data = json.load(f)
    DataInsert(json_data)