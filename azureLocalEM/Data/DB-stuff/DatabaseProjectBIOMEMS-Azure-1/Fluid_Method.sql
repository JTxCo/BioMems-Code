CREATE TABLE [dbo].[Fluid_Method]
(
  [fluid_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [sampleName] VARCHAR(13) NOT NULL,
  [method_name] VARCHAR(20) NOT NULL,
  [eChemName] VARCHAR(20) NOT NULL,
  [washName] VARCHAR(20) NOT NULL,
  [incubationTime] INT NOT NULL,
)
