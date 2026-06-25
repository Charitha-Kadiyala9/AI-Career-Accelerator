from google import genai


def get_client(api_key):
    return genai.Client(api_key=api_key)


# -----------------------------
# Resume Generator
# -----------------------------
def generate_resume(
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
):
    client = get_client(api_key)

    prompt = f"""
    Create a concise ATS-friendly ONE-PAGE resume.

    Template Type:
    {template}

    Name: {name}
    Phone: {phone}
    Email: {email}
    LinkedIn: {linkedin}
    Education: {education}
    Skills: {skills}
    Projects: {projects}
    Career Goal: {career_goal}

    Rules:

    - Maximum one page
    - Professional Summary: 2-3 lines only
    - Education section must be included
    - Skills in bullet points
    - Include only the 2 most important projects
    - Career Objective: 2 lines only
    - ATS-friendly formatting
    - Keep total length under 500 words
    - Avoid unnecessary explanations
    Use the provided phone number, email and LinkedIn URL.
    Do not leave placeholders.
    
    Do not write:
    [Phone Number]
    [Email Address]
    [LinkedIn URL]
    [Your Name]
    
    Use the actual values provided above.
    
    Format the resume with clear headings and bullet points.
    If LinkedIn URL is empty, do not mention LinkedIn.
    Do not use markdown symbols such as **, ##, or *.
    Return plain professional resume text only.
    Use this structure:

    NAME

    PROFESSIONAL SUMMARY

    EDUCATION

    SKILLS

    PROJECTS

    CAREER OBJECTIVE
    
    
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Cover Letter Generator
# -----------------------------
def generate_cover_letter(
    api_key,
    name,
    phone,
    email,
    linkedin,
    skills,
    career_goal
):
    client = get_client(api_key)

    prompt = f"""
    Write a concise professional cover letter.

    Name: {name}
    Phone: {phone}
    Email: {email}
    LinkedIn: {linkedin}
    Skills: {skills}
    Career Goal: {career_goal}
    
    
    Rules:

    - Maximum one page
    - 3 short paragraphs
    - Professional tone
    - Internship/job application format
    - Keep under 300 words
    Use the provided contact information.

    Do not write:
    [Phone Number]
    [Email Address]
    [LinkedIn URL]
    [Your Name]
    [Company Name]
    
    Use the actual values provided above.
    
    Add the applicant's name and contact details at the top.
    If LinkedIn URL is empty, do not mention LinkedIn.
    If company information is not provided,
    do not include Company Name,
    Company Address,
    Hiring Manager Name,
    or Hiring Manager Title.
    Start directly with:
    Dear Hiring Manager,
    and then continue the cover letter.
    
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# ATS Score Checker
# -----------------------------
def ats_score_checker(
        api_key,
        resume_text
):
    client = get_client(api_key)

    prompt = f"""
Act as a professional ATS evaluator.

Resume:

{resume_text}

Provide:

1. ATS Score out of 100
2. Strengths
3. Weaknesses
4. Missing Keywords
5. Suggestions to Improve ATS Score
6. Recruiter Feedback

Format clearly.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Skill Gap Analysis
# -----------------------------
def skill_gap_analysis(
        api_key,
        skills,
        career_goal
):
    client = get_client(api_key)

    prompt = f"""
Analyze the student profile.

Current Skills:
{skills}

Desired Career:
{career_goal}

Provide:

1. Existing Relevant Skills
2. Missing Skills
3. Certifications Recommended
4. Online Courses Recommended
5. Learning Roadmap
6. Estimated Preparation Time

Format professionally.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Career Roadmap Generator
# -----------------------------
def career_roadmap(
        api_key,
        career_goal
):
    client = get_client(api_key)

    prompt = f"""
Create a detailed 6-month roadmap.

Career Goal:
{career_goal}

Provide:

Month 1
Month 2
Month 3
Month 4
Month 5
Month 6

For each month include:

- Skills to learn
- Courses
- Certifications
- Projects

Make it practical.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# LinkedIn Optimizer
# -----------------------------
def linkedin_optimizer(
        api_key,
        name,
        skills,
        projects,
        career_goal
):
    client = get_client(api_key)

    prompt = f"""
Create a professional LinkedIn profile.

Name:
{name}

Skills:
{skills}

Projects:
{projects}

Career Goal:
{career_goal}

Generate:

1. LinkedIn Headline
2. About Section
3. Top Skills
4. Recruiter Keywords
5. Profile Improvement Tips

Make it highly professional.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text