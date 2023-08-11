import pyodbc
from table_BASE import BaseTable

class Fluid_Method(BaseTable):
    def __init__(self, sampleName, method_name, eChemName, washName, incubationTime) -> None:
        super().__init__()
        if None in (sampleName, method_name, eChemName, washName, incubationTime):
            raise ValueError("All attributes must be non-null.")
        if not isinstance(sampleName, str) or len(sampleName) > 13:
            raise ValueError("sampleName must be a string with a maximum length of 13 characters.")
        self.sampleName = sampleName
        if not isinstance(method_name, str) or len(method_name) > 20:
            raise ValueError("method_name must be a string with a maximum length of 20 characters.")
        self.method_name = method_name
        if not isinstance(eChemName, str) or len(eChemName) > 20:
            raise ValueError("eChemName must be a string with a maximum length of 20 characters.")
        self.eChemName = eChemName
        if not isinstance(washName, str) or len(washName) > 20:
            raise ValueError("washName must be a string with a maximum length of 20 characters.")
        self.washName = washName
        if not isinstance(incubationTime, int):
            raise ValueError("incubationTime must be an integer.")
        self.incubationTime = incubationTime