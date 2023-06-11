CREATE TABLE [dbo].[table1]
(
    [id] INT NOT NULL,
    [PatientID] VARCHAR(13) NOT NULL, 
    [PatientName] VARCHAR(20) NOT NULL,
    [DOB] DATE NOT NULL, 
    PRIMARY KEY CLUSTERED ([id] ASC)
)

-- INSERT INTO [dbo].[table1] ([id], [PatientID], [PatientName], [DOB])
-- VALUES (1, 'P123456789012', 'John Doe', '1990-01-01'),
--        (2, 'P987654321098', 'Jane Smith', '1985-03-15'),
--        (3, 'P456789012345', 'Bob Johnson', '1978-07-22');
