CREATE TABLE [dbo].[Well_Data]
(
  [well_data_ID] INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  [well_reference_ID] INT NOT NULL,
  CONSTRAINT [FK_Well_DATA_Well_Reference] FOREIGN KEY ([well_reference_ID]) REFERENCES [dbo].[Well_Reference] ([well_reference_ID]),
  [well_data] VARCHAR(4000) NOT NULL,
)
