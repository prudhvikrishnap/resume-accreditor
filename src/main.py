import streamlit as st
from PyPDF2 import PdfReader
from constants.constants import *

job_description_dict = {
    "front_end": [],
    "back_end": [],
    "programming_languages": []
}
job_description_details = st.text_area("Add Job Description Details")

for word in job_description_details.lower().split():
    if(word in JS_FRONTEND_FRAMEWORK_LIST):
        job_description_dict["front_end"].append(word)
    elif(word in JS_BACKEND_FRAMEWORK_LIST):
        job_description_dict["back_end"].append(word)
    elif(word in CORE_PROGRAMMING_LANGUAGES_LIST):
            job_description_dict["programming_languages"].append(word)
st.write(job_description_dict)

st.write("Resume Accreditor")
uploaded_file = st.file_uploader("Upload your resume here", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text = page.extract_text()
        st.write(text)