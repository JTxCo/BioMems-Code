CREATE TABLE [dbo].[Sample]
(
  [sample_ID] INT IDENTITY NOT NULL PRIMARY KEY,
  [test_ID] INT NOT NULL,
  CONSTRAINT [FK_Sample_Test_ID] FOREIGN KEY ([test_ID]) REFERENCES [dbo].[Test]([test_ID]),
)
