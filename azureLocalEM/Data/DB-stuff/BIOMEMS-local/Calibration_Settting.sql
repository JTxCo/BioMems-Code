CREATE TABLE [dbo].[Calibration_Settting]
(
  [calibration_ID] INT NOT NULL PRIMARY KEY IDENTITY(1000, 10),
  [dacOffset] INT(3) NOT NULL,
  [dacGain] INT(3) NOT NULL,
  [currentOffset] INT(4) NOT NULL,
  [shunt1Cal] INT(4) NOT NULL,
  [shunt2Cal] INT(4) NOT NULL,
  [shunt3Cal] INT(4) NOT NULL,
  [rangeSelect] INT(1) NOT NULL,
)
