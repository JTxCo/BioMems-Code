import os
import sys
import json 
# print(sys.path)

sys.path.append('azureLocalEm/Code/testFunctions/functionActions')
# print(sys.path)

path = "azureLocalEm/Code/testFunctions/functionActions"
print(os.listdir(path))

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

import db_test_upload

if 'db_test_upload' in globals():
    print('db_test_upload is in globals')
else:
    print('db_test_upload is not in globals')

# import db_test_upload

# from db_test_upload import DataInsert
# filepath = 'azureLocalEm/Data/jsonEXAMPLE2.json'
# with open(filepath, 'r') as f:
#     json_data = json.load(f)
#     DataInsert(json_data)