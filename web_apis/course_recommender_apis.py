from fastapi import FastAPI, HTTPException
import pyodbc

app = FastAPI()

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

# Database connection parameters
DB_SERVER = 'localhost\\BRAXTONS-LAPTOP'
DB_DATABASE = 'MIST460_RelationalDatabase_Lastname'
DB_USERNAME = 'your_username'
DB_PASSWORD = 'your_password'
DB_DRIVER = '{ODBC Driver 17 for SQL Server}'

def get_db_connection():
    try:
        conn_str = f'DRIVER={DB_DRIVER};SERVER={DB_SERVER};DATABASE={DB_DATABASE};trusted_connection=yes;'
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")
    
@app.get("/find_current_semester_course_offerings")
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

    # Convert rows to a list of dictionaries for better JSON serialization
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

@app.get("/find_prerequisites")
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

    # Convert rows to a list of dictionaries for better JSON serialization
    results = [
        {
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber
        }
        for row in rows
    ]

    return {"data": results}