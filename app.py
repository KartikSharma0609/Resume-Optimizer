import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

st.set_page_config(page_title="AI Career Architect", page_icon="🚀", layout="wide")

st.title("🚀 AI Career Architect")
st.markdown("### Optimize your resume & generate cover letters using Gemini 2.5")

with st.sidebar:
    st.header("Settings")
    
    # 1. Check if the Key is already in the System Secrets
    if "GOOGLE_API_KEY" in st.secrets:
        st.success("✅")
        api_key = st.secrets["GOOGLE_API_KEY"]
    else:
        # 2. If no secret key found, ask the user
        api_key = st.text_input("Enter Google API Key", type="password")
        if not api_key:
            st.warning("⚠️ Enter API Key to proceed.")
            st.stop()

# --- Initialize AI ---
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.7
    )
except Exception as e:
    st.error(f"Error: {e}")

# --- Functions ---
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# --- Main UI ---
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

with col2:
    job_desc = st.text_area("Paste Job Description", height=300)

# --- The Logic ---
if st.button("🚀 Launch Analysis", type="primary"):
    if uploaded_file and job_desc:
        with st.spinner("🤖 AI is analyzing... (this may take a few seconds)"):
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # Create Tabs
            tab1, tab2 = st.tabs(["📊 Analysis & Score", "✉️ Cover Letter"])

            # --- Tab 1: Analysis ---
            with tab1:
                analyze_prompt = PromptTemplate.from_template(
                    """
                    Act as a Senior Technical Recruiter.
                    Resume: {resume}
                    Job: {job}
                    
                    Provide a detailed analysis:
                    1. **Match Score**: (0-100)
                    2. **Missing Keywords**: List specific tools/skills missing.
                    3. **Profile Summary Rewrite**: Write a tailored 3-line summary.
                    """
                )
                chain_analyze = analyze_prompt | llm
                res_analysis = chain_analyze.invoke({"resume": resume_text, "job": job_desc})
                st.markdown(res_analysis.content)

            # --- Tab 2: Cover Letter ---
            with tab2:
                cover_letter_prompt = PromptTemplate.from_template(
                    """
                    Write a professional cover letter for this candidate.
                    Resume: {resume}
                    Job: {job}
                    
                    Tone: Professional, enthusiastic, and confident.
                    Focus: Highlight the skills that match the job description.
                    """
                )
                chain_cover = cover_letter_prompt | llm
                res_cover = chain_cover.invoke({"resume": resume_text, "job": job_desc})
                st.markdown(res_cover.content)
                
    else:

        st.warning("⚠️ Please upload a resume and paste a job description.")
