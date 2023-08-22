
DELETE FROM [BIOMEMS-local].[dbo].[Well_Data];
DELETE FROM [BIOMEMS-local].[dbo].[Well_Info];

DELETE FROM [BIOMEMS-local].[dbo].[Well_Reference];
DELETE FROM [BIOMEMS-local].[dbo].[Sample];
DELETE FROM [BIOMEMS-local].[dbo].[Cartridge];
DELETE FROM [BIOMEMS-local].[dbo].[Test];
DELETE FROM [BIOMEMS-local].[dbo].[PatientDevice];
DELETE FROM [BIOMEMS-local].[dbo].[Patient];
DELETE FROM [BIOMEMS-local].[dbo].[Device];
DELETE FROM [BIOMEMS-local].[dbo].[Calibration_Setting];
DELETE FROM [BIOMEMS-local].[dbo].[Fluid_Method];
DELETE FROM [BIOMEMS-local].[dbo].[TestTime];
-- EXEC sp_help PatientDevice;