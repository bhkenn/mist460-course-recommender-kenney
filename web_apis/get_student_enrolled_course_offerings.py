from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def get_student_enrolled_course_offerings(
    studentID: int
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL procGetStudentEnrolledCourseOfferings(?, ?)}", studentID)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    results = [
        {
            "StudentID": row.SubjectCode
        }
        for row in rows
    ]

    return {"data": results}