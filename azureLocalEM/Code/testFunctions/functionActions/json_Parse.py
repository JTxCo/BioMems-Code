# import json
import sys
import datetime
import os
<<<<<<< HEAD
import ast
import ujson as json
=======
>>>>>>> azurefunctions_helperfunctions
sys.path.append('azureLocalEm/Code/testFunctions/Classes')
relative_path = os.path.join(os.path.dirname(__file__), '../Classes')
sys.path.append(relative_path)

from table_Patient import Patient
from table_Device import Device
from table_Calibration_Setting import Calibration_Setting
from table_Test import Test
from table_Cartridge import Cartridge
from table_Fluid_Method import Fluid_Method
from table_TestTime import TestTime
from table_Well_Data import Well_Data
from table_Well_Info import Well_Info
from table_Well_Reference import Well_Reference
from table_PatientDevice import PatientDevice
from table_Sample import Sample

def parse_for_data(json_data):
    # for item in json_data["data"]["patientInfo"]:
        # print(f"Item: {item}")
    print("we are here before error ")
    if "data" in json_data:
        print("we are here after error ")
        data = json_data["data"]
        print("reuturning data")
        return data
       
def addPatient(data): 
    packetInfo = data["packetInfo"]
    patientInfo = packetInfo["patientInfo"]
    patientFirst = patientInfo["patientName"].split()[0]
    patientlast = patientInfo["patientName"].split()[1]
    patientID =patientInfo["patientID"]
    patientDOB_str = patientInfo["patientDOB"]
    try: 
        patientDOB = datetime.datetime.strptime(patientDOB_str, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Incorrect data format for patientDOB, should be YYYY.MM.DD")
    patient = Patient(patientID, patientFirst, patientlast, patientDOB)
    # print(f"patient: {patient.FirstName}")
    return patient

def addDevice(data):
    packetInfo = data["packetInfo"].keys()
    deviceInfo = data["packetInfo"]["deviceInfo"]
    instrumentID = deviceInfo["instrumentID"]
    errorServiceCode = deviceInfo["errorServiceCode"]
    cartirdgeInfo = data["packetInfo"]["cartridgeInfo"]
    GSID = cartirdgeInfo["GSID"]
    device = Device(instrumentID, errorServiceCode, GSID)
    return device
    # def addDevice

def addCalibrationSettings(data):
    calibrationSettings_str = data["packetInfo"]["calibrationSettings"]
    # calibrationSettings_dict = json.loads(calibrationSettings_str)
    calibrationSettings_dict = {key: int(value, 16) if value.startswith('0x') else int(value) for key, value in calibrationSettings_str.items()}
    # print(f"calibrationSettings: {calibrationSettings_dict}")
    calibrationSetting = Calibration_Setting(calibrationSettings_dict["dacOffset"], calibrationSettings_dict["dacGain"], calibrationSettings_dict["currentOffset"], calibrationSettings_dict["shunt1Cal"], calibrationSettings_dict["shunt2Cal"], calibrationSettings_dict["shunt3Cal"], calibrationSettings_dict["rangeSelect"])
    return calibrationSetting
    # def addCalibrationSettings

def addTest(data):
    operatorID = data["packetInfo"]["scanInfo"]["operatorID"]
    print(f"operatorID: {operatorID}")
    algorithmVersion = data["algorithmInfo"]["algorithmVersion"]
    sampleVersion = data["sampleInfo"]["sampleVersion"]
    test = Test(operatorID, int(algorithmVersion), int(sampleVersion))
    return test 

def addCartridge(data):
    cartirdgeInfo = data["packetInfo"]["cartridgeInfo"]
    GSID = cartirdgeInfo["GSID"]
    assayName = cartirdgeInfo["assayName"]
    cartridge = Cartridge(GSID, assayName)
    # print(f"cartridge: {cartridge.GSID}, {cartridge.assayName}")
    return cartridge
def addFluidMethod(data):
    fluidMethodInfo = data["packetInfo"]["fluidMethodInfo"]
    sampleName = fluidMethodInfo["sampleName"]
    methaod_name = fluidMethodInfo["methodName"]
    eCHemName = fluidMethodInfo["eChemName"]
    washName = fluidMethodInfo["washName"]
    incubationTime = int(fluidMethodInfo["incubationTime"])
    fluidMethod = Fluid_Method(sampleName, methaod_name, eCHemName, washName, incubationTime)
    return fluidMethod

def addTestTime(data):
    dateTime = data["packetInfo"]["dateTime"]
    # print(f"dateTime: {dateTime}")
    date = datetime.datetime.strptime(dateTime["date"], "%Y.%m.%d").date()
    time = datetime.datetime.strptime( dateTime["time"], "%H:%M:%S").time()
    timeZone = int(dateTime["timeZone"])
    testTime = TestTime(date, time, timeZone)
    return testTime

def addWellInfo(well_info_dict):
    # print("well_info: %s" % well_info_dict)
    well_X_info = Well_Info(json.dumps(well_info_dict))
    return well_X_info 

def addWellData(well_sample_list):
    list_well_class_data = [Well_Data(json.dumps(well_sample)) for well_sample in well_sample_list]
    return list_well_class_data
    
def addWellReferences(data):
    well_Reference_list = []
    sampleData = data["sampleData"]
    for well_name, well_data in sampleData.items():
        well_info_dict = well_data["info"]
        well_X_info = addWellInfo(well_info_dict)
        print("well_key: %s" % well_name)
        well_data = sampleData[well_name]
        well_X_data = well_data["sample"]
        list_well_X_info_data = addWellData(well_X_data) #list of all the samples of a well, X
        list_well_X_info_data.insert(0, well_X_info) #the info is added at the first position of the list
        well_X_reference = Well_Reference(list_well_X_info_data, well_name) #instance of a well reference
        well_Reference_list.append(well_X_reference)# add to list of instances of well references
    return well_Reference_list#list of all instanes of all well references
def addPatientDevice(patientID, instrumentID):
    patient_device = PatientDevice(patientID, instrumentID)
    return patient_device

def addSample(well_reference_list):
    sample = Sample(well_reference_list)
    return sample

# filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
# with open(filepath, 'r') as f:
#     json_data = json.load(f)
#     data = parse_for_data(json_data)
#     calibrationSetting = addCalibrationSettings(data)
#     device = addDevice(data)
#     patient = addPatient(data)        
#     test = addTest(data)
#     cartridge = addCartridge(data)
#     Fluid_Method = addFluidMethod(data)
#     testTIme = addTestTime(data)
#     wellReference_List = addWellReferences(data)




