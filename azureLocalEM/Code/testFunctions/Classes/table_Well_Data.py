import pyodbc
import json
from table_BASE import BaseTable

class Well_Data(BaseTable):
    def __init__(self, well_data) -> None:
        super().__init__()
        try: 
            json.loads(well_data)
        except json.JSONDecodeError:
            raise ValueError("Well Data must be a valid JSON string.")
        self.well_data = well_data 