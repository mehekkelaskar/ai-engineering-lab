from typing import List
from pydantic import BaseModel

# ----------------------------------------------------
# 1. API Request Model (What the user posts to backend)
# ----------------------------------------------------
class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description_text: str

# ----------------------------------------------------
# 2. LLM Extraction Models (For Tool / Parsing step)
# ----------------------------------------------------
class ExtractedResume(BaseModel):
    summary: str
    phone_number: str
    experience: List[str]
    projects: List[str]
    skills: List[str]
    education: List[str]

class ExtractedJD(BaseModel):
    job_title: str
    job_summary: str
    required_skills: List[str]
    preferred_skills: List[str]
    responsibilities: List[str]

# ----------------------------------------------------
# 3. Final Output Model (What API returns to user)
# ----------------------------------------------------
class AnalyzeResponse(BaseModel):
    match_score: float
    matching_skills: List[str]
    missing_skills: List[str]
    resume_issues: List[str]
    recommendations: List[str]