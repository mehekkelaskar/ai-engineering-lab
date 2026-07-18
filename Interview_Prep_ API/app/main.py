from fastapi import FastAPI
from app.api import topics, questions

app = FastAPI(
    title="Interview Preparation API",
    description="A foundational FastAPI practice project managing topics and questions.",
    version="1.0.0"
)

# Connect modular sub-routers
app.include_router(topics.router)
app.include_router(questions.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Interview Preparation API!",
        "docs_url": "/docs"
    }