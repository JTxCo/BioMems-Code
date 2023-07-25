import pyodbc
from table_BASE import BaseTable
from datetime import time

class TestTime(BaseTable):
    def __init__(self, Date, Time, TimeZone) :
        super().__init__()
        if None in (Date, Time, TimeZone):
            raise ValueError("All attributes must be non-null.")
        if not self.validate_Date(Date):
            raise TypeError("Date must be a datetime.date object.")
        self.Date = Date
        if not isinstance(Time, time):
            raise TypeError("Time must be a datetime.time object.") 
        self.Time = Time
        if not isinstance(TimeZone, str) or len(TimeZone) > 1:
            raise ValueError("TimeZone must be a string with a maximum length of 1 character.")
        self.TimeZone = TimeZone