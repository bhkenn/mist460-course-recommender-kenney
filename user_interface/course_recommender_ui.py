import pandas as pd
import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

def fetch_data(endpoint : str, params : dict, method: str = "get") -> pd.DataFrame:
    if method == "get":
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=params)
    elif method == "post":
        response = requests.post(f"{FASTAPI_URL}/{endpoint}", params=params)
    else:
        st.error(f"Unsupported HTTP method: {method}")
        return None

if response.status_code == 200:
    payload = response.json()
    rows = payload.get("data", [])
    df = pd.DataFrame(rows)
    return df

else:
    st.error(f"Error fetching data: {response.status_code}")
    return None

#create a sidebar with a dropdown to select the API endpoint
st.sidebar.title("Course Recommender Functionalities")
api_endpoint = st.sidebar.selectbox(
    "api endpoint",
    [
        "validate user",
        "find_current_semester_course_offerings",
        "find_prerequisites",
        "check_if_student_has_taken_all_prerequisites_for_course",
        "enroll_student_in_course_offering",
        "get_student_enrolled_course_offerings",
        "drop_student_from_course_offering"
    ]
)

if api_endpoint == "validate_user":
    st.header("Validate User")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Validate"):
        df = fetch_data("validate_user", {"username": username, "password": password})
        if df is not None:
            st.success("User validated successfully!")
        else:
            st.error("Invalid username or password.")