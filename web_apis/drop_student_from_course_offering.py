from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def drop_student_from_course_offering(
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
            "StudentID": row.StudentID,
            "CourseOfferingID": row.courseOfferingID
        }
        for row in rows
    ]

    return {"data": results}