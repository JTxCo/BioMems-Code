import json
import sys
import datetime
import ast
import ujson as json
sys.path.append('azureLocalEm/Code/Classes')


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

def parse(json_data):
    # for item in json_data["data"]["patientInfo"]:
        # print(f"Item: {item}")
    if "data" in json_data:
        data = json_data["data"]
        packetInfo = data["packetInfo"]
        patientInfo = packetInfo["patientInfo"]
        # calibrationSetting = addCalibrationSettings(data)
        # device = addDevice(data)
        # patient = addPatient(patientInfo)        
        # test = addTest(data)
        # cartridge = addCartridge(data)
        # Fluid_Method = addFluidMethod(data)
        # testTIme = addTestTime(data)
        addWellReferences(data)
        # addWellInfo(data)
        # print(f"patient: %s, device: %s, calibrationSetting: %d" % (patient.FirstName, device.instrumentID, calibrationSetting.dacOffset))

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
    print(f"calibrationSettings: {calibrationSettings_dict}")
    calibrationSetting = Calibration_Setting(calibrationSettings_dict["dacOffset"], calibrationSettings_dict["dacGain"], calibrationSettings_dict["currentOffset"], calibrationSettings_dict["shunt1Cal"], calibrationSettings_dict["shunt2Cal"], calibrationSettings_dict["shunt3Cal"], calibrationSettings_dict["rangeSelect"])
    return calibrationSetting
    # def addCalibrationSettings

def addTest(data):
    operatorID = data["packetInfo"]["scanInfo"]["operatorID"]
    algorithmVersion = data["algorithmInfo"]["algorithmVersion"]
    sampleVersion = data["sampleInfo"]["sampleVersion"]
    test = Test(operatorID, int(algorithmVersion), int(sampleVersion))
    return test 

def addCartridge(data):
    cartirdgeInfo = data["packetInfo"]["cartridgeInfo"]
    GSID = cartirdgeInfo["GSID"]
    assayName = cartirdgeInfo["assayName"]
    cartridge = Cartridge(GSID, assayName)
    print(f"cartridge: {cartridge.GSID}, {cartridge.assayName}")
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
    print(f"dateTime: {dateTime}")
    date = datetime.datetime.strptime(dateTime["date"], "%Y.%m.%d").date()
    time = datetime.datetime.strptime( dateTime["time"], "%H:%M:%S").time()
    timeZone = int(dateTime["timeZone"])
    testTime = TestTime(date, time, timeZone)
    return testTime 

def addWellReferences(data):
    sampleData = data["sampleData"]
    for well_key, well_data in sampleData.items():
        print("well_key: %s" % well_key)
        well_data = sampleData[well_key]
        print("header:" + join(well_data.keys()))
# def addWellInfo(data):

    
filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(filepath, 'r') as f:
    json_data = json.load(f)
    parse(json_data)



