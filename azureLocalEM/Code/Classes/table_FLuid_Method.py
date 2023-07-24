import pyodbc
from table_BASE import BaseTable

class Fluid_Method(BaseTable):
    def __init__(self, sampleName, method_name, eChemName, washName, incubationTime) -> None:
        super().__init__()
        self.sampleName = sampleName
        self.method_name = method_name
        self.eChemName = eChemName
        self.washName = washName
        self.incubationTime = incubationTime