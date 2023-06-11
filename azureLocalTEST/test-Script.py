import pyodbc

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=azureLocalTEST;"
    "Trusted_Connection=yes;"
)


conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM [dbo].[table1]")
rows = cursor.fetchone()

for row in rows:
    print(row)
    
    
cursor.execute("SELECT @@version")
row = cursor.fetchone()
print(row)
conn.close()