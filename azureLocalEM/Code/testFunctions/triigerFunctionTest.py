import requests
import json
import os



file_path = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(file_path, 'r') as f:
    json_data = f.read()

json_data  = json.dumps(json_data)
headers = {'Content-Type': 'application/json'}
url = 'http://localhost:7071/api/hello'
response = requests.post(url, data=json_data, headers=headers) 
print(response.content)
