import pyodbc
from table_BASE import BaseTable


class Device(BaseTable):
    def __intit__ (self, instrumentID, ServiceCode, GSID, test_ID, patiendID) -> None:
        super().__init__()
        self.instrumentID = instrumentID
        self.ServiceCode = ServiceCode
        self.GSID = GSID
        self.test_ID = test_ID
        self.patientID = patiendID
        