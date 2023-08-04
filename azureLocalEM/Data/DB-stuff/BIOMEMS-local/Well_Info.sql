CREATE TABLE [dbo].[Well_Info]
(
  [well_ID] INT NOT NULL PRIMARY KEY ,
  [well_info] VARCHAR(4000) NOT NULL,
  CONSTRAINT [FK_Well_Info_Well_ID] FOREIGN KEY ([well_ID]) REFERENCES [dbo].[Well_Reference]([well_ID])
)
