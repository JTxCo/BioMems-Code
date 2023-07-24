import xmltodict
import json

with open('azureLocalEM/Data/BioMems-XML-example.xml') as f:
    data = xmltodict.parse(f.read())
    json_data = json.dumps(data, indent=4)
    with open('azureLocalEM/Data/jsonEXAMPLE.json', 'w') as json_file:
        json_file.write(json_data)
