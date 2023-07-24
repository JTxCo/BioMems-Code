import pyodbc
class BaseTable():
    def __init__(self) -> None:
        self.server_name = "localhost"
        self.database_name = "azureLocalTEST"
        self.user_id = "testLogin"
        self.password = "$testPassword"
        self.conn_str = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={self.server_name};"
            f"Database={self.database_name};"
            f"UID={self.user_id};"
            f"PWD={self.password};"
        )
        self.conn = None
        self.cursor = None 
    def connect(self):
        self.conn = pyodbc.connect(self.conn_str)
    
    def execute(self, query):
        self.cursor = self.conn.cursor()    
        self.cursor.execute(query)

    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.conn.close()
        
        
    
    