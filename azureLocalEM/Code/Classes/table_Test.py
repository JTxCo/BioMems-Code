import pyodbc
from table_BASE import BaseTable

class Test(BaseTable):
    def __init__(self, operatorID: str, algorithmVersion: int, sampleVersion: int) :
        super().__init__()
        if None is (operatorID, algorithmVersion, sampleVersion):
            raise ValueError(" operatorID, algorithmInfo, sampleInfo must be non-null.")
        if not isinstance(operatorID, str) or len(operatorID) > 13:
            raise ValueError("operatorID must be a string with a maximum length of 50 characters.")
        self.operatorID = operatorID
        if not isinstance(algorithmVersion, int):
            raise TypeError("algorithmVersion must be an integer.")
        self.algorithmInfo = algorithmVersion
        if not isinstance(sampleVersion, int):
            raise TypeError("sampleVersion must be an integer.")
        self.sampleInfo = sampleVersion
    