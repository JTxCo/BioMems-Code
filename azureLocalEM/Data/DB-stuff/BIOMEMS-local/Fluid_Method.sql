CREATE TABLE [dbo].[Fluid_Method]
(
  [fluid_ID] INT NOT NULL PRIMARY KEY IDENTITY(1000, 10),
  [sampleName] VARCHAR(13) NOT NULL,
  [method_name] VARCHAR(20) NOT NULL,
  [eChemName] VARCHAR(20) NOT NULL,
  [washName] VARCHAR(20) NOT NULL,
  [incubationTime] INT(4) NOT NULL,
)
