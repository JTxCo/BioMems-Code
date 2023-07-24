import pyodbc
from table_BASE import BaseTable
CREATE TABLE [dbo].[TestTime]
(
  [time_ID] INT NOT NULL PRIMARY KEY IDENTITY,
  [Date] DATE NOT NULL,
  [Time] TIME NOT NULL,
  [TimeZone] VARCHAR(1) NOT NULL,
)


class TestTime(BaseTable):
    def __init__(self, time_ID, Date, Time, TimeZone) :
        super().__init__()
        self.time_ID = time_ID
        self.Date = Date
        self.Time = Time
        