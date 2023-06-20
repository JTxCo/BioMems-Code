CREATE TABLE [dbo].[Device]
(
  [instrumentID]  varchar(13) NOT NULL PRIMARY KEY,
  [errorServiceCode] varchar(8),
  [patientID] INT NOT NULL,
  FOREIGN KEY (patientID) REFERENCES Patient(patientID),
  [GSID] VARCHAR(13) NOT NULL,
  FOREIGN KEY (GSID) REFERENCES Catridge(GSID),
  [test_ID] INT NOT NULL,
  FOREIGN KEY (test_ID) REFERENCES Test(test_ID),
)
