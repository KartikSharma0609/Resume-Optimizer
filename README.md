# 🚀 AI Career Architect

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini_2.5-8E75B2.svg)

An intelligent, containerized Resume Optimization application designed to automate the tedious process of tailoring resumes for specific job descriptions. Powered by Google Gemini 2.5 and LangChain, this tool performs semantic gap analysis and generates tailored cover letters to help candidates stand out.

## ✨ Key Features
* **Smart PDF Parsing:** Securely extracts text from resumes while defending against decompression attacks.
* **Semantic Gap Analysis:** Moves beyond basic keyword matching to deeply analyze skill overlap with job descriptions.
* **Cover Letter Generation:** Automatically drafts professional, context-aware cover letters.
* **Enterprise Security:** Implements strict memory limits and upload size boundaries to ensure safe parsing.
* **Frictionless Deployment:** Fully containerized with Docker for immediate, "works-on-my-machine" reliability.

---

## 🐳 Run Instantly with Docker (Recommended)
You can test this application locally in seconds without installing Python dependencies or configuring a virtual environment. 

Ensure you have Docker installed, then run:
```bash
docker run -p 8501:8501 -m 512m -e GOOGLE_API_KEY="your_google_api_key" kartiksh2002/resume-optimizer:latest
