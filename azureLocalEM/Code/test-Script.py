import pyodbc

server_name = "localhost"
database_name = "azureLocalTEST"
user_id = "testLogin"
password = "$testPassword"

conn_str = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"UID={user_id};"
    f"PWD={password};"
)


conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM [dbo].[table1]")
rows = cursor.fetchall()

for row in rows:
    print("row: " +str(row))
    
cursor.execute("SELECT @@version")
row = cursor.fetchone()
print(row)
conn.close()