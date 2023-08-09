CREATE TABLE [dbo].[Device]
(
  [instrumentID]  varchar(13) NOT NULL PRIMARY KEY,
  [errorServiceCode] varchar(8), 
  [patientID] VARCHAR(13) NOT NULL,
  CONSTRAINT [FK_Device_Patient] FOREIGN KEY ([patientID]) REFERENCES [dbo].[Patient]([patientID]),
  [GSID] VARCHAR(13) NOT NULL,
  constraint [FK_Device_GSID] foreign key ([GSID]) references [dbo].[Catridge]([GSID]),
  [test_ID] INT NOT NULL,
  CONSTRAINT [FK_Device_test_ID] FOREIGN KEY ([test_ID]) REFERENCES [dbo].[Test]([test_ID])
)
