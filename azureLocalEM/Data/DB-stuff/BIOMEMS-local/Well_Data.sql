CREATE TABLE [dbo].[Well_Data]
(
  [well_ID] INT NOT NULL PRIMARY KEY,
  [well_data] VARCHAR(4000) NOT NULL,
  CONSTRAINT [FK_Well_Data_Well_ID] FOREIGN KEY ([well_ID]) REFERENCES [dbo].[Well_Info]([well_ID])
)
