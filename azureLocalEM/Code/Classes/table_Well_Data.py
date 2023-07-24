import pyodbc
from table_BASE import BaseTable

class Well_Data(BaseTable):
    def __init__(self, well_data) -> None:
        super().__init__()
        self.well_data = well_data 
