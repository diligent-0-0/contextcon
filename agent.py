import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AQ.Ab8RN6Iz3wUYy30GfzTacLZnLwsRQVHledkEZNyZlxNMBpaXtw")

# Fast Generation Config
FAST_CONFIG = {
    "temperature": 0.1,         # Low temperature = faster greedy decoding
    "max_output_tokens": 500,   # Prevents long, verbose responses
    "top_p": 0.8
}

@st.cache_data(show_spinner=False)
def evaluate_match(candidate_profile: str, job_description: str, company_data: dict):
    model = genai.GenerativeModel('gemini-3.8-flash')
    prompt = f"""
    You are FairMatch AI, an objective career mediator.
    Company: {company_data}
    Job: {job_description}
    Candidate: {candidate_profile}
    
    Provide a concise dual evaluation in Markdown:
    ### 🎯 CANDIDATE PERSPECTIVE
    - **Match Score**: (0-100%)
    - **Why This Fits**: (2 key bullet points)
    - **Company Reality Check**: (1 bullet based on Crustdata)
    - **Gap & Action Plan**: (1 bullet)
    
    ### 👔 HR / RECRUITER PERSPECTIVE
    - **Match Score**: (0-100%)
    - **Candidate Strengths**: (2 key bullet points)
    - **Potential Risks**: (1 bullet)
    - **Recommended Action**: (Screen / Pass)
    """
    response = model.generate_content(prompt, generation_config=FAST_CONFIG)
    return response.text

@st.cache_data(show_spinner=False)
def generate_recruiter_email(candidate_profile: str, company_name: str, role_title: str):
    model = genai.GenerativeModel('gemini-3.8-flash')
    prompt = f"""
    Draft a 4-sentence cold outreach email from a candidate to a recruiter at {company_name} for {role_title}.
    Candidate Highlights: {candidate_profile}
    Keep it concise, confident, and include a clear call-to-action for a 15-min chat.
    Return Subject Line and Body.
    """
    response = model.generate_content(prompt, generation_config=FAST_CONFIG)
    return response.text

@st.cache_data(show_spinner=False)
def find_hiring_managers(company_name: str, role_title: str):
    model = genai.GenerativeModel('gemini-3.8-flash')
    prompt = f"""
    Identify 3 likely hiring decision-makers for '{role_title}' at '{company_name}'.
    For each provide:
    - Name & Title
    - Likely Corporate Email (e.g. name@company.com)
    - Confidence Score
    Keep output concise.
    """
    response = model.generate_content(prompt, generation_config=FAST_CONFIG)
    return response.text