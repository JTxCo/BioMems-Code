import pyodbc
from table_BASE import BaseTable

class Patient(BaseTable):
    def __init__(self, ID, FirstName, LastName, DOB) -> None:
        super().__init__()
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DOB = DOB       
        
     
