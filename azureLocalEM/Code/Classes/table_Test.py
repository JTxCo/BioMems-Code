import pyodbc
from table_BASE import BaseTable

class Test(BaseTable):
    def _init__(self, operatorID):
        super().__init__()
        if None is (operatorID):
            raise ValueError("operatorID must be non-null.")
        if not isinstance(operatorID, str) or len(operatorID) > 13:
            raise ValueError("operatorID must be a string with a maximum length of 50 characters.")
        self.operatorID = operatorID
    
    