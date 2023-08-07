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

from json_Parse import parse_for_data, addPatient, addDevice, addCalibrationSettings, addFluidMethod, addTestTime, addCalibrationSettings, addCartridge, addTest, addWellData, addWellInfo, addWellReference

def patientInsert(patient: Patient):
    patient.connect()
    query = f"INSERT INTO [dbo].[Patient] ([patientID], [patientFirstName], [patientLastName], [patientDOB]) VALUES ('{patient.ID}', '{patient.FirstName}', '{patient.LastName}', '{patient.DOB}')"
    patient.execute(query)
    patient.commit()
    patient.close()
    
def deviceInsert(device: Device, patientID: str):
    device.connect()
    query = f"INSERT INTO [dbo].[Device] ([instrumentID], [errorServiceCode],[patientID], [GSID]) VALUES ('{device.instrumentID}',   '{device.errorServiceCode}','{patientID}',  '{device.GSID}')"
    device.execute(query)
    device.commit()
    device.close()

def fluidMethodInsert(fluidMethod: Fluid_Method):
    fluidMethod.connect()
    query = f"INSERT INTO [dbo].[Fluid_Method] ([sampleName], [method_name], [eChemName], [washName], [incubationTime]) VALUES ('{fluidMethod.sampleName}', '{fluidMethod.method_name}', '{fluidMethod.eChemName}', '{fluidMethod.washName}', '{fluidMethod.incubationTime}')"
    fluidMethod.execute(query)
    fluidMethod.commit()
    fluidMethod.close()
    
    
def CalibrationSettingInsert(calibrationSetting: Calibration_Setting):
    calibrationSetting.connect()
    query = f"INSERT INTO [dbo].[Calibration_Setting] ([dacOffset], [dacGain], [currentOffset], [shunt1Cal], [shunt2Cal], [shunt3Cal], [rangeSelect]) VALUES ('{calibrationSetting.dacOffset}', '{calibrationSetting.dacGain}', '{calibrationSetting.currentOffset}', '{calibrationSetting.shunt1Cal}', '{calibrationSetting.shunt2Cal}', '{calibrationSetting.shunt3Cal}', '{calibrationSetting.rangeSelect}')"
    calibrationSetting.execute(query)
    calibrationSetting.commit()
    calibrationSetting.close()
    

def TestTimeInsert(testTime: TestTime):
    testTime.connect()
    query = f"INSERT INTO [dbo].[TestTime] ([Date], [Time], [TimeZone]) VALUES ('{testTime.Date}', '{testTime.Time}', '{testTime.TimeZone}')"
    testTime.execute(query)
    testTime.commit()
    testTime.close()
    
def CartridgeInsert(cartridge: Cartridge, test_ID: int):
    cartridge.connect()
    query = f"INSERT INTO [dbo].[Cartridge] ([GSID], [Assay_Name], [test_ID]) VALUES ('{cartridge.GSID}', '{cartridge.Assay_Name}', '{test_ID}')"
    cartridge.execute(query)
    cartridge.commit()
    cartridge.close()    


def TestInsert(test: Test, fluid_ID: int, calibration_ID: int, time_ID: int, well_reference_ID: int):
    test.connect()
    query = f"INSERT INTO [dbo].[Test] ([operatorID], [algorithmVersion], [sampleVersion], [fluid_ID], [calibration_ID], [time_ID], [well_reference_ID])  VALUES ('{test.operatorID}', '{test.algorithmVersion}', '{test.sampleVersion}', '{fluid_ID}', '{calibration_ID}', '{time_ID}', '{well_reference_ID}')"
    test.execute(query)
    test.commit()
    test.close()


def Well_Info_Insert(wellInfo: Well_Info):
    wellInfo.connect()
    query = f"INSERT INTO [dbo].[Well_Info] ([well_info]) OUTPUT inserted.[well_info_ID] VALUES ('{wellInfo.well_info}')"
    wellInfo.execute(query)
    well_info_ID = wellInfo.fetchone()[0]
    wellInfo.commit()
    wellInfo.close()
    return well_info_ID

def Well_Data_Insert(wellData: Well_Data):
    wellData.connect()
    query = f"INSERT INTO [dbo].[Well_Data] ([well_data]) OUTPUT inserted.[well_data_ID] VALUES ('{wellData.well_data}')"
    wellData.execute(query)
    well_data_ID = wellData.fetchone()[0]
    wellData.commit()
    wellData.close()
    return well_data_ID

def Well_Reference_Insert(wellReference: Well_Reference, well_info_ID: int, well_data_ID: int):
    wellReference.connect()
    query = f"INSERT INTO [dbo].[Well_Reference] ([well_info_ID], [well_data_ID]) VALUES ('{well_info_ID}', '{well_data_ID}')"
    wellReference.execute(query)
    wellReference.commit()
    wellReference.close()

filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
with open(filepath, 'r') as f:
    json_data = json.load(f)
    data = parse_for_data(json_data)
    patient = addPatient(data)
    # patientInsert(patient)
    # device = addDevice(data)
    # deviceInsert(device, patient.ID)
    fluidMethod = addFluidMethod(data)
    fluidMethodInsert(fluidMethod)
    

