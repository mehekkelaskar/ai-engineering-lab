# app/services.py

from fastapi import APIRouter, HTTPException
from app.model import AnalyzeRequest, AnalyzeResponse
from app.llm_client import analyze_resume_with_llm

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/", response_model=AnalyzeResponse)
def analyze_resume(payload: AnalyzeRequest):
    try:
        # Pass raw input to our LLM pipeline
        result = analyze_resume_with_llm(
            resume_text=payload.resume_text,
            job_description_text=payload.job_description_text
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))