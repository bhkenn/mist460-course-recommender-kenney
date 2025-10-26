from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def find_current_prerequisites(
    subject_code: str,
    course_number: str
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL proceFindPrerequisites(?, ?)}", subject_code, course_number)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    results = [
        {
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber
        }
        for row in rows
    ]

    return {"data": results}