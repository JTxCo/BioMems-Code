import requests
import json
import os




file_path = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(file_path, 'r') as f:
    json_data = f.read()
    headers = {'Content-Type': 'application/json'}
    url = 'http://localhost:7071/api/hello'
    try:
        response = requests.post(url, data=json_data, headers=headers) 
        response_content = response.content.decode('utf-8')
        print(response_content)
    except Exception as e:
        print("Failed: " +str(e))
