import requests
import json
import os

# data = {
#   "patientInfo": {
#     "patientID": "abcdefghijklm",
#     "patientName": "Leslie Nielsen",
#     "patientDOB": "1926.02.11"
#   }
# }

file_path = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(file_path, 'rb') as f:
    json_data = f.read()

json_data  = json.dumps(json_data)
headers = {'Content-Type': 'application/json'}
url = 'http://localhost:7071/api/hello'
response = requests.post(url, data=json_data, headers=headers) 
print(response.content)
# result = response.json()
# print("result: " + str(result))