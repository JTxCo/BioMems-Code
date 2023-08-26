import sys
import json
import os
import logging


parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

current_file_path = os.path.abspath(__file__)
relative_path = os.path.join(os.path.dirname(__file__), '../Classes')
sys.path.append(relative_path)
sys.path.append('azureLocalEm/Code/testFunctions/functionActions')
sys.path.append('azureLocalEm/Code/testFunctions/Classes')
from Classes.table_BASE import BaseTable
from table_BASE import BaseTable
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

from functionActions.json_Parse import parse_for_data, addPatient, addDevice, addCalibrationSettings, addFluidMethod, addTestTime, addCalibrationSettings, addCartridge, addTest, addWellData, addWellInfo, addWellReferences, addPatientDevice, addSample

# current_dir = os.path.dirname(os.path.realpath(__file__))
# print(f"current_dir: {current_dir}")



def RemoveConstraint(constraint: str, table: str):
    base = BaseTable()
    base.connect()
    query = f"ALTER TABLE [dbo].[{table}] DROP CONSTRAINT {constraint}"
    base.execute(query)
    base.commit()
    base.close()
    
def AddConstraint(constraint: str, table: str):
    base = BaseTable()
    base.connect()
    query = f"ALTER TABLE [dbo].[{table}] ADD CONSTRAINT {constraint}"
    base.execute(query)
    base.commit()
    base.close()
    
def patientInsert(patient: Patient):
    patient.connect()
    query = f"INSERT INTO [dbo].[Patient] ([patientID], [patientFirstName], [patientLastName], [patientDOB]) VALUES ('{patient.ID}', '{patient.FirstName}', '{patient.LastName}', '{patient.DOB}')"
    patient.execute(query)
    patient.commit()
    patient.close()

def fluidMethodInsert(fluidMethod: Fluid_Method):
    fluidMethod.connect()
    query = f"INSERT INTO [dbo].[Fluid_Method] ([sampleName], [method_name], [eChemName], [washName], [incubationTime]) OUTPUT inserted.[fluid_ID] VALUES ('{fluidMethod.sampleName}', '{fluidMethod.method_name}', '{fluidMethod.eChemName}', '{fluidMethod.washName}', '{fluidMethod.incubationTime}')"
    fluidMethod.execute(query)
    fluid_ID = fluidMethod.fetchone()[0]
    fluidMethod.commit()
    fluidMethod.close()
    return fluid_ID
    
def CalibrationSettingsInsert(calibrationSetting: Calibration_Setting):
    calibrationSetting.connect()
    query = f"INSERT INTO [dbo].[Calibration_Setting] ([dacOffset], [dacGain], [currentOffset], [shunt1Cal], [shunt2Cal], [shunt3Cal], [rangeSelect]) OUTPUT inserted.[calibration_ID] VALUES ('{calibrationSetting.dacOffset}', '{calibrationSetting.dacGain}', '{calibrationSetting.currentOffset}', '{calibrationSetting.shunt1Cal}', '{calibrationSetting.shunt2Cal}', '{calibrationSetting.shunt3Cal}', '{calibrationSetting.rangeSelect}')"
    calibrationSetting.execute(query)
    calibration_ID = calibrationSetting.fetchone()[0]
    calibrationSetting.commit()
    calibrationSetting.close()
    return calibration_ID

def TestTimeInsert(testTime: TestTime):
    testTime.connect()
    query = f"INSERT INTO [dbo].[TestTime] ([Date], [Time], [TimeZone]) OUTPUT inserted.[time_ID] VALUES ('{testTime.Date}', '{testTime.Time}', '{testTime.TimeZone}')"
    testTime.execute(query)
    time_ID = testTime.fetchone()[0]
    testTime.commit()
    testTime.close()
    return time_ID

def Well_Info_Insert(wellInfo: Well_Info, well_reference_ID: int):
    wellInfo.connect()
    query = f"INSERT INTO [dbo].[Well_Info] ([well_reference_ID], [well_info]) OUTPUT inserted.[well_info_ID] VALUES ('{well_reference_ID}','{wellInfo.well_info}')"
    wellInfo.execute(query)
    well_info_ID = wellInfo.cursor.fetchone()[0]
    wellInfo.commit()
    wellInfo.close()
    return well_info_ID

def Well_Data_Insert(wellData: Well_Data, well_reference_ID: int):
    wellData.connect()
    query = f"INSERT INTO [dbo].[Well_Data] ([well_reference_ID], [well_data]) OUTPUT inserted.[well_data_ID] VALUES ('{well_reference_ID}','{wellData.well_data}')"
    wellData.execute(query)
    well_data_ID = wellData.cursor.fetchone()[0]
    wellData.commit()
    wellData.close()
    return well_data_ID

def Well_Reference_Insert(wellReference: Well_Reference, sample_ID: int):
    wellReference.connect()
    query = f"INSERT INTO [dbo].[Well_Reference] ([sample_ID], [well_name]) OUTPUT inserted.[well_reference_ID] VALUES ('{sample_ID}', '{wellReference.well_name}')"
    wellReference.execute(query)
    well_reference_id = wellReference.cursor.fetchone()[0]
    wellReference.commit()
    wellReference.close()
    return well_reference_id
    
def TestInsert(test: Test, instrumentID, fluid_ID: int, calibration_ID: int, time_ID: int):
    test.connect()
    query = f"INSERT INTO [dbo].[Test] ([operatorID], [algorithmVersion], [sampleVersion], [instrumentID],[fluid_ID], [calibration_ID], [time_ID]) OUTPUT inserted.[test_ID] VALUES ('{test.operatorID}', '{test.algorithmVersion}', '{test.sampleVersion}', '{instrumentID}', '{fluid_ID}', '{calibration_ID}', '{time_ID}')"
    test.execute(query)
    test_ID = test.cursor.fetchone()[0]
    test.commit()
    test.close()
    return test_ID

def deviceInsert(device: Device):
    device.connect()
    query = f"INSERT INTO [dbo].[Device] ([instrumentID], [errorServiceCode]) VALUES ('{device.instrumentID}', '{device.errorServiceCode}')"
    device.execute(query)
    device.commit()
    device.close()
    
def PatientDeviceInsert(patientDevice: PatientDevice):
    patientDevice.connect()
    query = f"INSERT INTO [dbo].[PatientDevice] ([patientID], [instrumentID]) VALUES ('{patientDevice.patientID}', '{patientDevice.instrumentID}')"
    patientDevice.execute(query)
    patientDevice.commit()
    patientDevice.close()
  
def CartridgeInsert(cartridge: Cartridge,instrumentID: str, test_ID: int):
    cartridge.connect()
    query = f"INSERT INTO [dbo].[Cartridge] ([GSID], [Assay_Name],[instrumentID], [test_ID]) VALUES ('{cartridge.GSID}', '{cartridge.Assay_Name}','{instrumentID}', '{test_ID}')"
    cartridge.execute(query)
    cartridge.commit()
    cartridge.close()

def SampleInsert(sample: Sample, test_ID: int):
    sample.connect()
    query = f"INSERT INTO [dbo].[Sample] ( [test_ID]) OUTPUT inserted.[sample_ID] VALUES ('{test_ID}')"
    sample.execute(query)
    sample_ID = sample.cursor.fetchone()[0]
    sample.commit()
    sample.close()
    return sample_ID


# filepath = 'azureLocalEm/Data/jsonEXAMPLE.json'
# with open(filepath, 'r') as f:
#     json_data = json.load(f)

def DataInsert(json_data):   
    data = parse_for_data(json_data)
    try: 
        patient = addPatient(data)
        patientInsert(patient)
        print("Patient Inserted")
        
        device = addDevice(data)
        print(f"Device: {device.instrumentID}, Error Code: {device.errorServiceCode}, GSID: {device.GSID}")
        deviceInsert(device)
        print("Device Inserted")
        
        patientDevice = addPatientDevice(patient.ID, device.instrumentID)
        PatientDeviceInsert(patientDevice)
        print("Patient Device Inserted")
        
        fluidMethod = addFluidMethod(data)
        fluid_ID = fluidMethodInsert(fluidMethod)
        print("FLuid inserted with id: " + str(fluid_ID))
        
        print("Calibration Setting")        
        Calibration_Setting = addCalibrationSettings(data)
        calibration_ID = CalibrationSettingsInsert(Calibration_Setting)
        print("Calibration inserted with id: " + str(calibration_ID))
        
        print("Test Time")
        testTime = addTestTime(data)
        # print(f"Date: {testTime.Date}, Time: {testTime.Time}, TimeZone: {testTime.TimeZone}")
        time_ID = TestTimeInsert(testTime)
        print("Time inserted with id: " + str(time_ID))
        
        print("Test table begin")
        test = addTest(data)
        test_ID = TestInsert(test, device.instrumentID, fluid_ID, calibration_ID, time_ID)
        print("Test table inserted with id: " + str(test_ID))
        
        print("well and sample begin")
        well_reference_list = addWellReferences(data)
        sample = addSample(well_reference_list)
        sample_ID = SampleInsert(sample, test_ID)
        print("Sample inserted with id: " + str(sample_ID))
        well_reference_ID = Well_Reference_Insert(well_reference_list[0], sample_ID)
        cartridge = addCartridge(data)
        CartridgeInsert(cartridge,device.instrumentID, test_ID) 
        print("Cartridge inserted")
        well_info = well_reference_list[0].well_list_info_data[0]
        well_info_ID = Well_Info_Insert(well_info, well_reference_ID)
        print("well info id: " + str(well_info_ID))
        well_data = well_reference_list[0].well_list_info_data[1]
        # print(well_data.well_data)
        well_data_ID = Well_Data_Insert(well_data, well_reference_ID)
        print("well data id: " + str(well_data_ID))
        
    except Exception as e:
        logging.info("Failed in data insert.")
        raise
