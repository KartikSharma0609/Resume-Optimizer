AI Career Architect

**Live Demo:** resume-optimizer-euftnywe4korzfy5ykghck
.streamlit.app

Overview
The **AI Career Architect** is a Resume Optimization tool powered by **Google Gemini 2.5**. It helps job seekers automated the tedious process of tailoring resumes for specific job applications. 

Instead of generic keyword matching, this tool uses Large Language Models (LLMs) to understand the semantic meaning of a resume and provides a comprehensive gap analysis and a tailored cover letter.

Tech Stack
* **Core Logic:** Python 3.10+
* **AI Engine:** Google Gemini 2.5 Flash (via LangChain)
* **Frontend:** Streamlit
* **PDF Processing:** PyPDF2

Key Features
* **Smart Parsing:** Extracts text from PDF resumes accurately.
* **Gap Analysis:** Compares candidate skills vs. Job Description requirements to calculate a "Match Score."
* **Cover Letter Generation:** Automatically writes a professional cover letter highlighting relevant experience.
* **Secure:** Supports API Key injection for secure usage.

How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-career-architect.git](https://github.com/YOUR_USERNAME/ai-career-architect.git)
   cd ai-career-architect
