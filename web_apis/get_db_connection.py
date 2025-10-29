from fastapi import FastAPI, HTTPException

import pyodbc #Python Open DataBase Connectivity library

import os

from dotenv import load_dotenv

from pathlib import Path

# Load environment variables from .env file

path = Path(__file__).parent.parent / '.env'

load_dotenv(dotenv_path=path)



def get_db_connection():


  environment = os.getenv('ENVIRONMENT')

  if environment == 'PRODUCTION':

    DB_SERVER = os.getenv('DB_SERVER')

    DB_DATABASE = os.getenv('DB_NAME')

    DB_USERNAME = os.getenv('DB_USER')

    DB_PASSWORD = os.getenv('DB_PASSWORD')

    DB_DRIVER = os.getenv('DB_DRIVER')

    connection_string = (   

      f'DRIVER={DB_DRIVER};'

      f'SERVER={DB_SERVER};'

      f'DATABASE={DB_DATABASE};'

      f'UID={DB_USERNAME};'

      f'PWD={DB_PASSWORD};'

      'Encrypt=yes;'

      'TrustServerCertificate=no;'

      'Connection Timeout=30;'

    )

  else:

    #Development environment settings

    DB_SERVER = 'localhost\\BRAXTONS-LAPTOP'

    DB_DATABASE = 'MIST460_RelationalDatabase_Lastname'

    DB_DRIVER = '{ODBC Driver 18 for SQL Server}'

    connection_string = (   

      f'DRIVER={DB_DRIVER};'    

      f'SERVER={DB_SERVER};'

      f'DATABASE={DB_DATABASE};'

      'Encrypt=yes;'

      'Trusted_Connection=yes;'

      'Connection Timeout=30;'

      'TrustServerCertificate=yes;'

    )


  try:

    return pyodbc.connect(connection_string)

  except Exception as e:

    raise HTTPException(status_code=500, detail="Database connection error")