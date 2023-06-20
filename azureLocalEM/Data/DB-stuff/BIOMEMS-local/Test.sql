CREATE TABLE [dbo].[Test]
(
  [test_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [fluid_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Fluid_ID] FOREIGN KEY ([fluid_ID]) REFERENCES [dbo].[Fluid_Method]([fluid_ID]),
  [calibration_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Calibration_ID] FOREIGN KEY ([calibration_ID]) REFERENCES [dbo].[Calibration_Settting]([calibration_ID]),
  [time_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Time_ID] FOREIGN KEY ([time_ID]) REFERENCES [dbo].[TestTime]([time_ID]),
  [well_reference_ID] INT NOT NULL,
  CONSTRAINT [FK_Test_Well_Reference_ID] FOREIGN KEY ([well_reference_ID]) REFERENCES [dbo].[Well_reference]([well_reference_ID]),
)
