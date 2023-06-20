CREATE TABLE [dbo].[Catridge]
(
  [GSID] VARCHAR(13) NOT NULL PRIMARY KEY,
  [Assay_Name] VARCHAR(13),
  [test_ID] INT NOT NULL,
  FOREIGN KEY (test_ID) REFERENCES Test(test_ID),
)
