import pyodbc
from table_BASE import BaseTable

class Cartridge(BaseTable):
    def __init__(self, GSID, assayName) -> None:
        super().__init__()
        if None is (GSID):
            raise ValueError("GSID must be non-null.")
        if not isinstance(GSID, str) or len(GSID) > 13:
            raise ValueError("GSID must be a string with a maximum length of 50 characters.")
        self.GSID = GSID
        if not isinstance(assayName, str) or len(assayName) > 20:
            raise ValueError("assayName must be a string with a maximum length of 50 characters.")
        self.assayName = assayName
        
    
        