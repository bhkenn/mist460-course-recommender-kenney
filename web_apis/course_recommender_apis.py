from fastapi import FastAPI, HTTPException
import pyodbc
from validate_user import validate_user
from find_current_semester_course_offerings import find_current_semester_course_offerings
from find_prerequisites import find_current_prerequisites
from check_if_student_has_taken_all_prerequisites_for_course import check_if_student_has_taken_all_prerequisites_for_course
from get_student_enrolled_course_offerings import get_student_enrolled_course_offerings

app = FastAPI()

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
    
@app.get("/validate_user/")
def validate_user_api(username: str, password: str):
    return validate_user(username, password)

@app.get("/find_current_semester_course_offerings/")
def find_current_semester_course_offerings_api( subjectCode: str, courseNumber: str):
    return find_current_semester_course_offerings(subjectCode, courseNumber)

@app.get("/find_prerequisites/")
def find_current_prerequisites_api( subjectCode: str, courseNumber: str):
    return find_current_prerequisites(subjectCode, courseNumber)

@app.get("/check_if_student_has_taken_all_prerequisites_for_course/")
def check_if_student_has_taken_all_prerequisites_for_course_api( studentID: int, subjectCode: str, courseNumber: str):
    return check_if_student_has_taken_all_prerequisites_for_course(studentID, subjectCode, courseNumber)

@app.post("/enroll_student_in_course_offering/")
def enroll_student_in_course_offering_api( studentID: int, courseOfferingID: int):
    return enroll_student_in_course_offering(studentID, courseOfferingID)

@app.get("/get_student_enrolled_course_offerings/")
def get_student_enrolled_course_offerings_api( studentID: int):
    return get_student_enrolled_course_offerings(studentID)