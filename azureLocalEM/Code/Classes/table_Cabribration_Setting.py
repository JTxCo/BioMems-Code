import pyodbc
from table_BASE import BaseTable
class Calribration_Setting(BaseTable):
    def __init__(self, dacOffset, dacGain, currentOffset, shunt1Cal, shunt2Cal, shunt3Cal, rangeSelect) -> None:
        super().__init__()
        if None in (dacOffset, dacGain, currentOffset, shunt1Cal, shunt2Cal, shunt3Cal, rangeSelect):
            raise ValueError("All attributes must be non-null.")
        if not all(isinstance(item, int) for item in (dacOffset, dacGain, currentOffset, shunt1Cal, shunt2Cal, shunt3Cal, rangeSelect)):
            raise ValueError("All attributes must be integers.")
        self.dacOffset = dacOffset
        self.dacGain = dacGain
        self.currentOffset = currentOffset
        self.shunt1Cal = shunt1Cal
        self.shunt2Cal = shunt2Cal
        self.shunt3Cal = shunt3Cal
        self.rangeSelect = rangeSelect
        
    