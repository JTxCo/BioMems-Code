import pyodbc
from table_BASE import BaseTable

class Well_Reference(BaseTable):
    def __init__(self, well_class_list) -> None:
        super().__init__()
        self.well_class_list = well_class_list