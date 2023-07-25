import pyodbc
from table_BASE import BaseTable


class Device(BaseTable):
    def __intit__ (self, instrumentID: str, ServiceCode: str, GSID: str, test_ID: int, ) -> None:
        super().__init__()
        if not isinstance(instrumentID, str) or len(instrumentID) > 50 or None:
            raise ValueError("instrumentID must be a string with a maximum length of 50 characters.")
        self.instrumentID = instrumentID

        self.ServiceCode = ServiceCode
        self.GSID = GSID
        self.test_ID = test_ID
        