import pyodbc
import datetime
from table_BASE import BaseTable

class Patient(BaseTable):
    def __init__(self, ID : str, FirstName: str, LastName: str, DOB: datetime.date) -> None:
        super().__init__()
        if None in (ID, FirstName, LastName, DOB):
            raise ValueError("All attributes must be non-null.")
        if not isinstance(ID, str) or len (ID) > 13:
            raise ValueError("ID must be a string with a maximum length of 13 characters.")
        self.ID = ID
        if not isinstance(FirstName, str) or len(FirstName) > 50: 
            raise ValueError("FirstName must be a string with a maximum length of 50 characters.")
        self.FirstName = FirstName
        if not isinstance(LastName, str) or len(LastName) > 50:
            raise ValueError("LastName must be a string with a maximum length of 50 characters.")
        self.LastName = LastName
        if not self.validate_Date(DOB):
           raise TypeError("DOB must be a datetime.date object.") 
        self.DOB = DOB       
        
     
    