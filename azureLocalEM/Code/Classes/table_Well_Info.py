import pyodbc
import json
from table_BASE import BaseTable

class Well_Info(BaseTable):
    def __init__(self, well_info:json ) -> None:
        super().__init__()
        try:
            json.loads(well_info)
        except json.JSONDecodeError:
            raise ValueError("Well Info must be a valid JSON string.")
        self.well_info = well_info

        
