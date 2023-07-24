import pyodbc
from table_BASE import BaseTable

class Well_Info(BaseTable):
    def __init__(self, well_info) -> None:
        super().__init__()
        self.well_info = well_info
        
