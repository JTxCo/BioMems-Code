import pyodbc
from table_BASE import BaseTable



class Calribration_Setting(BaseTable):
    def __init__(self, dacOffset, dacGain, currentOffset, shunt1Cal, shunt2Cal, shunt3Cal, rangeSelect) -> None:
        super().__init__()
        self.dacOffset = dacOffset
        self.dacGain = dacGain
        self.currentOffset = currentOffset
        self.shunt1Cal = shunt1Cal
        self.shunt2Cal = shunt2Cal
        self.shunt3Cal = shunt3Cal
        self.rangeSelect = rangeSelect
        
    