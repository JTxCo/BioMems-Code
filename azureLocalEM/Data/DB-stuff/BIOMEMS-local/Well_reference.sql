CREATE TABLE [dbo].[Well_Reference]
(
  [well_reference_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [sample_ID] INT NOT NULL,
  CONSTRAINT [FK_Well_Reference_Sample_ID] FOREIGN KEY ([sample_ID]) REFERENCES [dbo].[Sample]([sample_ID]),
  [well_name] NVARCHAR(50) NOT NULL,
)
