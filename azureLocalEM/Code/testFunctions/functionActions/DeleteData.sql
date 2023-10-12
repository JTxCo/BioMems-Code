
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Well_Data];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Well_Info];

DELETE FROM [BIOMEMS-Azure-1].[dbo].[Well_Reference];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Sample];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Cartridge];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Test];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[PatientDevice];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Patient];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Device];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Calibration_Setting];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[Fluid_Method];
DELETE FROM [BIOMEMS-Azure-1].[dbo].[TestTime]; 

-- EXEC sp_help PatientDevice;