import pyodbc
import datetime
class BaseTable():
    def __init__(self) -> None:
        self.local_server_name = "localhost"
        self.cloud_server_name = "tcp:biomems-azure-1.database.windows.net,1433;"
        
        self.local_database_name = "BIOMEMS-local"
        self.cloud_database_name = "BIOMEMS-Azure-1"
        
        self.local_user_id = "sa"
        self.cloud_user_id = "BIOMEMS-admin"
        
        self.local_password = "P@ssword"
        self.cloud_password = "BIOP@sswordMEM"
        
        self.local_conn_str = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={self.local_server_name};"
            f"Database={self.local_database_name};"
            f"UID={self.local_user_id};"
            f"PWD={self.local_password};"
        )
        self.cloud_conn_str =(
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server=tcp:biomems-azure-1.database.windows.net,1433;"
            f"Database=BIOMEMS-Azure-1;"
            f"Uid=BIOMEMS-admin;"
            f"Pwd={self.cloud_password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
        )
        self.conn = None
        self.cursor = None 
    def connect(self, database_type='cloud'):
        if database_type == 'cloud':
            self.conn = pyodbc.connect(self.cloud_conn_str)
        else:
            self.conn = pyodbc.connect(self.local_conn_str)
    
    def execute(self, query):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)

    def commit(self):
        if self.conn: 
            self.conn.commit()
        
    def close(self):
        if self.conn: 
            self.conn.close()

    def fetchone(self):
        if self.cursor:
            return self.cursor.fetchone()
    def validate_Date(self, DOB):
        return datetime.datetime.strftime(DOB, '%Y-%m-%d') == DOB.strftime('%Y-%m-%d')
    
    