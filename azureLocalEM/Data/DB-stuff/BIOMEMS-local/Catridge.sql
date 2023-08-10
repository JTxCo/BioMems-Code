CREATE TABLE [dbo].[Cartridge]
(
  [GSID] VARCHAR(13) NOT NULL PRIMARY KEY,
  [Assay_Name] VARCHAR(20),
  [instrumentID]  VARCHAR(13) NOT NULL, 
  CONSTRAINT [FK_Cartridge_InstrumentID] FOREIGN KEY ([instrumentID]) REFERENCES [dbo].[Device]([instrumentID]),
  [test_ID] INT NOT NULL,
  CONSTRAINT [FK_Catridge_Test_ID] FOREIGN KEY ([test_ID]) REFERENCES [dbo].[Test]([test_ID]),
)

