import pyodbc
from table_BASE import BaseTable


class Device(BaseTable):
    def __intit__ (self, instrumentID: str, errorServiceCode: str,patientID: str, GSID: str) -> None:
        super().__init__()
        if None in (instrumentID, GSID, patientID):
            raise ValueError("Attributes:  must be non-null.")
        if not isinstance(instrumentID, str) or len(instrumentID) > 13:
            raise ValueError("instrumentID must be a string with a maximum length of 50 characters.")
        self.instrumentID = instrumentID
        if errorServiceCode is not None:
            if not isinstance(errorServiceCode, str) or len(errorServiceCode) > 8:
                raise ValueError("errorServiceCode must be a string with a maximum length of 50 characters.")
        self.errorServiceCode = errorServiceCode
        if not isinstance(patientID, str) or len(patientID) > 13:
            raise ValueError("patientID must be a string with a maximum length of 50 characters.")
        self.patientID = patientID 
        if not isinstance(GSID, str) or len(GSID) > 13:
            raise ValueError("GSID must be a string with a maximum length of 50 characters.")
        self.GSID = GSID
        
        