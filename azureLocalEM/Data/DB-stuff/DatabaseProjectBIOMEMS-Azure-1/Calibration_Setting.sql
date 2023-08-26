CREATE TABLE [dbo].[Calibration_Setting]
(
  [calibration_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [dacOffset] INT NOT NULL,
  [dacGain] INT NOT NULL,
  [currentOffset] INT NOT NULL,
  [shunt1Cal] INT NOT NULL,
  [shunt2Cal] INT NOT NULL,
  [shunt3Cal] INT NOT NULL,
  [rangeSelect] INT NOT NULL
)