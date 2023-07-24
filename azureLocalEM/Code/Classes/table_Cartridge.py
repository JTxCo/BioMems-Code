import pyodbc
from table_BASE import BaseTable

class Cartridge(BaseTable):
    def __init__(self, GSID, Assay_Name) -> None:
        super().__init__()
        self.GSID = GSID
        self.Assay_Name = Assay_Name
        
    
        