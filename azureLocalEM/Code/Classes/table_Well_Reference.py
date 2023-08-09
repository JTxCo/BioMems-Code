import pyodbc
from table_BASE import BaseTable

class Well_Reference(BaseTable):
    def __init__(self, well_list_info_data, well_name: str) -> None:
        super().__init__()
        self.well_list_info_data = well_list_info_data
        self.well_name = well_name