import pyodbc
from table_BASE import BaseTable

class Well_Reference(BaseTable):
    def __init__(self, well_class_list, well_name: str) -> None:
        super().__init__()
        self.well_class_list = well_class_list
        self.well_name = well_name