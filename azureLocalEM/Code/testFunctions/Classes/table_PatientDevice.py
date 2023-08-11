from table_BASE import BaseTable 

class PatientDevice(BaseTable):
    def __init__(self, patientID, instrumentID) -> None:
        super().__init__()
        if None in (patientID, instrumentID):
            raise ValueError("All attributes must be non-null.")
        if not isinstance(patientID, str) or len (patientID) > 13:
            raise ValueError("patientID must be a string with a maximum length of 13 characters.")
        self.patientID = patientID
        if not isinstance(instrumentID, str) or len(instrumentID) > 13:
            raise ValueError("instrumentID must be a string with a maximum length of 13 characters.")
        self.instrumentID = instrumentID
        
        