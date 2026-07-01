import streamlit as st
from pdf_reader import extract_text
from analyzer import analyze_resume


st.title("AI Resume Analyzer", width = 500)

uploaded_file = st.file_uploader("Upload your resume(PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Analyse Resume"):
        with st.spinner("Analyzing Resume..."):

           resume_text = extract_text(uploaded_file)

           if not resume_text.strip():
               st.error("Data is not extracted")
           else:
                result = analyze_resume(resume_text)

                st.subheader("Analysis completed")

                st.write(result)


