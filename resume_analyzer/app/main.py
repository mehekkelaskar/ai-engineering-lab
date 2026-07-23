from fastapi import FastAPI
from app.services import router as analyze_router

app=FastAPI()
app.include_router(analyze_router)

@app.get("/")   
def read_root():
    return {"message": "Welcome to the Resume Analyzer API!"}   