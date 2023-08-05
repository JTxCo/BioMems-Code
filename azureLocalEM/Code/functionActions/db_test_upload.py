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

from json_Parse import parse_for_data, addPatient, addDevice, addCalibrationSettings, addFluidMethod

def patientInsert(patient: Patient):
    patient.connect()
    query = f"INSERT INTO [dbo].[Patient] ([patientID], [patientFirstName], [patientLastName], [patientDOB]) VALUES ('{patient.ID}', '{patient.FirstName}', '{patient.LastName}', '{patient.DOB}')"
    patient.execute(query)
    patient.commit()
    patient.close()
    
def deviceInsert(device: Device, patientID: str):
    device.connect()
    query = f"INSERT INTO [dbo].[Device] ([instrumentID], [errorServiceCode],[patientID], [GSID]) VALUES ('{device.instrumentID}', '{patientID}'  '{device.errorServiceCode}', '{device.GSID}')"
    device.execute(query)
    device.commit()
    device.close()

def fluidMethodInsert(fluidMethod: Fluid_Method):
    fluidMethod.connect()
    query = f"INSERT INTO [dbo].[Fluid_Method] ([sampleName], [method_name], [eChemName], [washName], [incubationTime]) VALUES ('{fluidMethod.sampleName}', '{fluidMethod.method_name}', '{fluidMethod.eChemName}', '{fluidMethod.washName}', '{fluidMethod.incubationTime}')"
    fluidMethod.execute(query)
    fluidMethod.commit()
    fluidMethod.close()
filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(filepath, 'r') as f:
    json_data = json.load(f)
    data = parse_for_data(json_data)
    patient = addPatient(data)
    # patientInsert(patient)
    # device = addDevice(data)
    # deviceInsert(device)
    fluidMethod = addFluidMethod(data)
    fluidMethodInsert(fluidMethod)
    

