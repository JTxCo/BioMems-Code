CREATE TABLE [dbo].[Well_Reference]
(
  [well_reference_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [well_ID] INT NOT NULL,
  CONSTRAINT [FK_Well_Reference_Well_ID_in_WELl-INFO] FOREIGN KEY ([well_ID]) REFERENCES [dbo].[Well_Info]([well_ID]), 
  CONSTRAINT [FK_Well_Reference_Well_ID_in_WELl-DATA] FOREIGN KEY ([well_ID]) REFERENCES [dbo].[Well_Data]([well_ID]),
)
