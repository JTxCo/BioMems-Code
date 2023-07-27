CREATE TABLE [dbo].[PatientDevice] (
  [patientID]  varchar(13) NOT NULL,
  [instrumentID] VARCHAR(13) NOT NULL,
  CONSTRAINT PK_PatientDevice_Comp PRIMARY KEY (patientID, instrumentID),
  CONSTRAINT FK_PatientDevice_Patient FOREIGN KEY (patientID) REFERENCES Patient (patientID),
  CONSTRAINT FK_PatientDevice_Device FOREIGN KEY (instrumentID) REFERENCES Device (instrumentID)
);
