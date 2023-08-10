import pyodbc
from table_BASE import BaseTable


class Device(BaseTable):
    def __init__ (self, instrumentID: str, errorServiceCode: str, GSID: str) -> None:
        super().__init__()
        if None in (instrumentID, GSID):
            raise ValueError("Attributes:  must be non-null.")
        if not isinstance(instrumentID, str) or len(instrumentID) > 13:
            raise ValueError("instrumentID must be a string with a maximum length of 13 characters.")
        self.instrumentID = instrumentID
        if errorServiceCode is not None:
            if not isinstance(errorServiceCode, str) or len(errorServiceCode) > 8:
                raise ValueError("errorServiceCode must be a string with a maximum length of 50 characters.")
        self.errorServiceCode = errorServiceCode
        if not isinstance(GSID, str) or len(GSID) > 13:
            raise ValueError("GSID must be a string with a maximum length of 50 characters.")
        self.GSID = GSID
        
        