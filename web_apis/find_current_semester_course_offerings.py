from fastapi import FastAPI, HTTPException
import pyodbc
from get_db_connection import get_db_connection

def find_current_semester_course_offerings(
    subject_code: str,
    course_number: str
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL proceFindCurrentSemesterCourseOfferingsForSpecificCourse(?, ?)}", subject_code, course_number)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    results = [
        {
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber,
            "CRN": row.CRN,
            "Semester": row.CourseOfferingSemester,
            "Year": row.CourseOfferingYear,
            "CourseOfferingID": row.CourseOfferingID,
            "NumberSeatsRemaining": row.NumberSeatsRemaining
        }
        for row in rows
    ]

    return {"data": results}
