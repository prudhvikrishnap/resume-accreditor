import streamlit as st
from PyPDF2 import PdfReader

st.write("Resume Accreditor")
uploaded_file = st.file_uploader("Upload your resume here", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text = page.extract_text()
        st.write(text)
