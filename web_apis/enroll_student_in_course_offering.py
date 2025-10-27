from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def enroll_student_in_course_offering(
    studentID: int,
    courseOfferingID: int
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL procDropStudentFromCourseOfferingCalled(?, ?)}", studentID, courseOfferingID)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    results = [
        {
            "EnrollmentResponse": row.EnrollmentResponse,
            "EnrollmentSucceeded": row.EnrollmentSucceeded
        }
        for row in rows
    ]

    return {"data": results}