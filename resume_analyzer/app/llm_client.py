# app/llm_client.py

import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from google import genai
from google.genai import types
from app.model import AnalyzeResponse
from app.tools import calculate_match_score

# Initialize Gemini Client (Ensure GEMINI_API_KEY is set in your environment variables)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def analyze_resume_with_llm(resume_text: str, job_description_text: str) -> AnalyzeResponse:
    prompt = f"""
    You are an expert HR Analyst.
    Compare the following Resume and Job Description.

    1. Extract matching and missing skills.
    2. CALL the `calculate_match_score` tool to calculate the exact match_score based on matching and missing skills.
    3. Identify resume issues and produce actionable recommendations.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description_text}
    """

    # 1. Call Gemini with Tools and Structured Response specification
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(
            # Register the tool function
            tools=[calculate_match_score],
            # Force response structure matching Pydantic class
            response_mime_type="application/json",
            response_schema=AnalyzeResponse,
            temperature=0.2,
        ),
    )

    # 2. Return validated Pydantic object
    return response.parsed