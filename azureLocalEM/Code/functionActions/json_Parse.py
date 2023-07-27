import json
import sys
sys.path.append('azureLocalEm/Code/Classes')
from table_Patient import Patient
import datetime

def parse(json_data):
    # for item in json_data["data"]["patientInfo"]:
        # print(f"Item: {item}")
    if "data" in json_data:
        data = json_data["data"]
        packetInfo = data["packetInfo"]
        patientInfo = packetInfo["patientInfo"]
        patient = addPatient(patientInfo)        
        # patientInfo = data.get("patientInfo", {})

def addPatient(patientInfo):
    # for key, value in patientInfo.items():
        # print(f"key: {key}, value: {value}")
    patientFirst = patientInfo["patientName"].split()[0]
    patientlast = patientInfo["patientName"].split()[1]
    # print(f"patientFirst: {patientFirst}, patientLast: {patientlast}")
    patientID =patientInfo["patientID"]
    patientDOB_str = patientInfo["patientDOB"]
    try: 
        patientDOB = datetime.datetime.strptime(patientDOB_str, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Incorrect data format for patientDOB, should be YYYY.MM.DD")
    patient = Patient(patientID, patientFirst, patientlast, patientDOB)
    print(f"patient: {patient.FirstName}")
    return patient

filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(filepath, 'r') as f:
    json_data = json.load(f)
    parse(json_data)



