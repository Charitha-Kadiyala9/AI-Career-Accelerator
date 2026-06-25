import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
st.write("Loaded Key:", api_key)
import streamlit as st
from pdf_generator import (
    create_resume_pdf,
    create_cover_letter_pdf
)

from ai_engine import (
    generate_resume,
    generate_cover_letter,
    ats_score_checker,
    skill_gap_analysis,
    career_roadmap,
    linkedin_optimizer
)


# ==========================
# PAGE SETTINGS
# ==========================
st.set_page_config(
    page_title="AI Career Accelerator",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #0E1117;
    color: #FFFFFF;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0F62FE;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Titles */
h1 {
    color: #FFFFFF;
    font-weight: bold;
}

h2, h3 {
    color: #78A9FF;
}

/* Labels */
label {
    color: #FFFFFF !important;
    font-weight: 500;
}

/* Text Inputs */
.stTextInput input,
.stTextArea textarea {
    background-color: #1C1F26;
    color: white;
    border-radius: 10px;
    border: 1px solid #3B82F6;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: #1C1F26;
    color: white;
}

/* Buttons */
.stButton > button {
    background-color: #0F62FE;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #0353E9;
}

/* Success Messages */
.stSuccess {
    background-color: #1E4620;
    color: white;
}

/* Info Boxes */
[data-testid="stMarkdownContainer"] {
    color: white;
}

/* Radio Buttons */
.stRadio label {
    color: white !important;
}

/* Download Buttons */
.stDownloadButton > button {
    background-color: #24A148;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stDownloadButton > button:hover {
    background-color: #198038;
}

</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Career Accelerator")

st.markdown("""
### Powered by Gemini AI

Generate:
- Professional Resume & Cover Letter
- ATS Score Report
- Skill Gap Analysis
- Career Roadmap
- LinkedIn Optimization
""")

# ==========================
# SIDEBAR MENU
# ==========================
st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose a Service",
    [
        "Resume & Cover Letter",
        "ATS Score Checker",
        "Skill Gap Analysis",
        "Career Roadmap",
        "LinkedIn Optimizer"
    ]
)

# =====================================================
# RESUME & COVER LETTER
# =====================================================
if option == "Resume & Cover Letter":

    st.header("📄 Resume & Cover Letter Generator")

    name = st.text_input("Full Name")

    phone = st.text_input("Phone Number")

    email = st.text_input("Email Address")

    linkedin = st.text_input(
        "LinkedIn Profile URL (Optional)"
    )

    education = st.text_area("Education")

    skills = st.text_area("Skills")

    projects = st.text_area("Projects")

    career_goal = st.text_input("Career Goal")

    template = st.selectbox(
        "Resume Template",
        [
            "Fresher",
            "Professional",
            "Creative Portfolio"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        generate_resume_btn = st.button("📄 Generate Resume")

    with col2:
        generate_cover_btn = st.button("✉️ Generate Cover Letter")

    # =========================
    # RESUME
    # =========================
    if generate_resume_btn:

        with st.spinner("Generating Resume..."):
            resume = generate_resume(
                api_key,
                template,
                name,
                phone,
                email,
                linkedin,
                education,
                skills,
                projects,
                career_goal
            )

        st.success("Resume Generated")

        st.subheader("📄 Resume Preview")

        st.text_area(
            "Resume Preview",
            resume,
            height=500
        )

        resume_pdf = create_resume_pdf(resume)

        with open(resume_pdf, "rb") as file:

            st.download_button(
                label="📥 Download Resume PDF",
                data=file,
                file_name="Resume.pdf",
                mime="application/pdf"
            )

    # =========================
    # COVER LETTER
    # =========================
    if generate_cover_btn:

        with st.spinner("Generating Cover Letter..."):
            cover_letter = generate_cover_letter(
                api_key,
                name,
                phone,
                email,
                linkedin,
                skills,
                career_goal
            )

        st.success("Cover Letter Generated")

        st.subheader("✉️ Cover Letter Preview")

        st.text_area(
            "Cover Letter Preview",
            cover_letter,
            height=350
        )

        cover_pdf = create_cover_letter_pdf(
            cover_letter
        )

        with open(cover_pdf, "rb") as file:

            st.download_button(
                label="📥 Download Cover Letter PDF",
                data=file,
                file_name="Cover_Letter.pdf",
                mime="application/pdf"
            )
# =====================================================
# ATS SCORE CHECKER
# =====================================================
elif option == "ATS Score Checker":

    st.header("🎯 ATS Resume Checker")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["txt"]
    )

    if uploaded_file is not None:

        resume_text = uploaded_file.read().decode("utf-8")

        if st.button("Check ATS Score"):

            with st.spinner("Analyzing Resume..."):

                ats_report = ats_score_checker(
                    api_key,
                    resume_text
                )

            st.success("Analysis Completed")

            st.write(ats_report)

# =====================================================
# SKILL GAP ANALYSIS
# =====================================================
elif option == "Skill Gap Analysis":

    st.header("📈 Skill Gap Analysis")

    skills = st.text_area("Current Skills")

    career_goal = st.text_input(
        "Desired Career"
    )

    if st.button("Analyze Skills"):

        with st.spinner("Analyzing..."):

            result = skill_gap_analysis(
                api_key,
                skills,
                career_goal
            )

        st.success("Analysis Completed")

        st.write(result)

# =====================================================
# CAREER ROADMAP
# =====================================================
elif option == "Career Roadmap":

    st.header("🛣 Career Roadmap Generator")

    career_goal = st.text_input(
        "Career Goal"
    )

    if st.button("Generate Roadmap"):

        with st.spinner("Generating Roadmap..."):

            roadmap = career_roadmap(
                api_key,
                career_goal
            )

        st.success("Roadmap Generated")

        st.write(roadmap)

# =====================================================
# LINKEDIN OPTIMIZER
# =====================================================
elif option == "LinkedIn Optimizer":

    st.header("💼 LinkedIn Profile Optimizer")

    name = st.text_input("Full Name")

    skills = st.text_area("Skills")

    projects = st.text_area("Projects")

    career_goal = st.text_input(
        "Career Goal"
    )

    if st.button("Optimize LinkedIn Profile"):

        with st.spinner("Optimizing..."):

            linkedin_content = linkedin_optimizer(
                api_key,
                name,
                skills,
                projects,
                career_goal
            )

        st.success("Optimization Completed")

        st.write(linkedin_content)