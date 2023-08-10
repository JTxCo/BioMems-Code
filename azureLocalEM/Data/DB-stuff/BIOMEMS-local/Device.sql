CREATE TABLE [dbo].[Device]
(
  [instrumentID]  varchar(13) NOT NULL PRIMARY KEY,
  [errorServiceCode] varchar(8), 
  -- [GSID] VARCHAR(13) NOT NULL,
  -- constraint [FK_Device_GSID] foreign key ([GSID]) references [dbo].[Catridge]([GSID]),
)
