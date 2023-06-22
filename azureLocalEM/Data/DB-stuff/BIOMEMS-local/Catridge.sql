CREATE TABLE [dbo].[Catridge]
(
  [GSID] VARCHAR(13) NOT NULL PRIMARY KEY,
  [Assay_Name] VARCHAR(20),
  [test_ID] INT NOT NULL,
  CONSTRAINT [FK_Catridge_Test_ID] FOREIGN KEY ([test_ID]) REFERENCES [dbo].[Test]([test_ID]),
)
