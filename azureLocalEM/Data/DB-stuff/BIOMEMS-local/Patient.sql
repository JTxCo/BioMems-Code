CREATE TABLE [dbo].[Patient]
(
  [patientID] INT NOT NULL PRIMARY KEY,
  [patientFirstName] VARCHAR(50) NOT NULL,
  [patientLastName] VARCHAR(50) NOT NULL,
  [patientDOB] DATE NOT NULL,
)
