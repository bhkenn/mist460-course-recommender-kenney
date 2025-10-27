from fastapi import FastAPI, HTTPException
import pyodbc

#DB_SERVER = 'mist-kenney.database.windows.net'
#DB_DATABASE = 'MIST460_RelationalDatabase_Kenney'
#DB_DRIVER = '{ODBC Driver 17 for SQL Server}'

DB_SERVER = 'localhost\\BRAXTONS-LAPTOP'
DB_DATABASE = 'MIST460_RelationalDatabase_Lastname'
DB_DRIVER = '{ODBC Driver 17 for SQL Server}'

def get_db_connection():
    try:
        conn_str = f'DRIVER={DB_DRIVER};SERVER={DB_SERVER};DATABASE={DB_DATABASE};trusted_connection=yes;'
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")