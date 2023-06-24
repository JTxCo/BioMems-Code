import xmltodict
import json
import os
with open('../Data/BioMems-XML-example.xml') as f:
    data = xmltodict.parse(f.read())
    json_data = json.dumps(data)
    print(json_data)




# path = '../Data/'
# cwd = os.getcwd()
# filesCWD = os.listdir(cwd)
# filesPath = os.listdir(path)
# print(f"Files in {path}: {filesPath}")
# print(f"Files in swd: {filesCWD}")
