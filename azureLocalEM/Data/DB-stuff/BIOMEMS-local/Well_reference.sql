CREATE TABLE [dbo].[Well_Reference]
(
  [well_reference_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [well_info_ID] INT NOT NULL UNIQUE,
  CONSTRAINT [FK_Well_REFERENCE_Info_ID] FOREIGN KEY ([well_info_ID]) REFERENCES [dbo].[Well_Info]([well_info_ID]),
  [well_data_ID] INT NOT NULL UNIQUE,
  CONSTRAINT [FK_Well_REFERENCE_Data_ID] FOREIGN KEY ([well_data_ID]) REFERENCES [dbo].[Well_Data]([well_data_ID])
)
