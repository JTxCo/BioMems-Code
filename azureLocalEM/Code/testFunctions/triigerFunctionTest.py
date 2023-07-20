import requests
import json
import os
#http sending stuff might use later
# file_path = '../../Data/BioMems-XML-example.xml'
# with open(file_path, 'rb') as f:
#     data = f.read()
#     headers = {'Content-Type': 'application/xml'}
#     response = requests.post(url, data=data, headers=headers)

# print(response.text)
# path = '../../Data/'
# cwd = os.getcwd()
# filesCWD = os.listdir(cwd)
# filesPath = os.listdir(path)
# print(f"Files in {path}: {filesPath}")
# print(f"Files in swd: {filesCWD}")


data = {
  "patientInfo": {
    "patientID": "abcdefghijklm",
    "patientName": "Leslie Nielsen",
    "patientDOB": "1926.02.11"
  }
}


json_data  = json.dumps(data)
headers = {'Content-Type': 'application/json'}
url = 'http://localhost:7071/api/hello'
response = requests.post(url, data=json_data, headers=headers) 
print(response.content)
# result = response.json()
# print("result: " + str(result))