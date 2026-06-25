# 🚀 AI Career Accelerator

## Overview

AI Career Accelerator is an AI-powered career development platform built using Streamlit, Google Gemini AI, and ReportLab.

The application helps students and job seekers create professional career documents and gain personalized career insights through AI-driven analysis.

---

## Problem Statement

Many students and job seekers struggle to create professional resumes, cover letters, and career plans that meet industry standards.

Traditional resume builders provide static templates but do not offer personalized recommendations, ATS analysis, career guidance, or skill-gap identification.

AI Career Accelerator solves this problem by leveraging Generative AI to provide intelligent career assistance.

---

## Features

### 📄 Resume Generator

* Generates ATS-friendly resumes
* Multiple resume templates
* Professional formatting
* PDF download support

### ✉️ Cover Letter Generator

* Creates professional cover letters
* Tailored to user skills and career goals
* PDF download support

### 🎯 ATS Score Checker

* Evaluates resume compatibility with Applicant Tracking Systems (ATS)
* Identifies strengths and weaknesses
* Suggests improvements and missing keywords

### 📊 Skill Gap Analysis

* Compares existing skills with career goals
* Identifies missing skills
* Recommends learning resources
* Provides improvement suggestions

### 🛣️ Career Roadmap Generator

* Generates personalized career paths
* Suggests certifications and learning milestones
* Provides step-by-step career guidance

### 💼 LinkedIn Profile Optimizer

* Reviews LinkedIn profile information
* Suggests profile improvements
* Generates better headlines and summaries
* Enhances professional visibility

---

## Technologies Used

* Python
* Streamlit
* Google Gemini AI
* ReportLab
* Python Dotenv

---

## Project Architecture

User Input
↓
Streamlit Frontend
↓
Google Gemini AI
↓
AI Analysis & Content Generation
↓
PDF Generation using ReportLab
↓
Results Displayed to User

---

## Project Structure

AI-Career-Accelerator/

├── app.py

├── ai_engine.py

├── pdf_generator.py

├── README.md

├── requirements.txt

├── .gitignore

├── .env

└── .venv/

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Career-Accelerator.git
```

### Navigate to Project Folder

```bash
cd AI-Career-Accelerator
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a file named `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Job Description Match Analyzer
* AI Interview Preparation
* Portfolio Website Generator
* Resume Ranking System
* Job Recommendation Engine

---

## Results

The application successfully generates:

* Professional ATS-friendly resumes
* Cover letters
* ATS reports
* Skill-gap analysis reports
* Career roadmaps
* LinkedIn profile optimization suggestions

---

## Author

**Kadiyala Charitha**

IBM SkillsBuild Internship Project

2026
