CREATE TABLE [dbo].[Test]
(
  [test_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [operatorID] VARCHAR(13) NOT NULL,
  [algorithmVersion] INT NOT NULL,
  [sampleVersion] INT NOT NULL,
  [instrumentID] VARCHAR(13) NOT NULL,
  CONSTRAINT [FK_TEST_INSTRUMENT_ID] FOREIGN KEY ([instrumentID]) REFERENCES [dbo].[Device]([instrumentID]),
  [fluid_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Fluid_ID] FOREIGN KEY ([fluid_ID]) REFERENCES [dbo].[Fluid_Method]([fluid_ID]),
  [calibration_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Calibration_ID] FOREIGN KEY ([calibration_ID]) REFERENCES [dbo].[Calibration_Setting]([calibration_ID]),
  [time_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Time_ID] FOREIGN KEY ([time_ID]) REFERENCES [dbo].[TestTime]([time_ID]),
)
