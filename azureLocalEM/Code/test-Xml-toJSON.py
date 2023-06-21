import xmltodict
import json
import os
# with open('./Data/BioMems-XML-example.xml') as f:
#     data = xmltodict.parse(f.read())
#     json_data = json.dumps(data)
#     print(json_data)

cwd = os.getcwd()
path = ''
files = os.listdir()
print("Files in %r. the path: %r : files: %s" % (cwd,path, files))