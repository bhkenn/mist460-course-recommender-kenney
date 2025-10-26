from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def check_if_student_has_taken_all_prerequisites_for_course(
    studentID: int,
    subject_code: str,
    course_number: str
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL procCheckIfStudentHasTakenAllPrerequisitesForCourse(?, ?)}", studentID, subject_code, course_number)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    results = [
        {
            "StudentID": row.StudentID,
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber
        }
        for row in rows
    ]

    return {"data": results}