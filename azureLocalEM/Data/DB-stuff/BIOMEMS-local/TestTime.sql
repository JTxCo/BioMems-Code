CREATE TABLE [dbo].[TestTime]
(
  [time_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [Date] DATE NOT NULL,
  [Time] TIME NOT NULL,
  [TimeZone] VARCHAR(1) NOT NULL,
)
