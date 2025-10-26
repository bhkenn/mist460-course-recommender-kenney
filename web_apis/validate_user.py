from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def validate_user(
    username: str,
    password: str
):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("{call procValidateUser(?,?)}", (username, password))

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    results = [
        {"AppUserID": row.AppUserID, "FullName": row.FullName}
    ]
    return {"data": results}