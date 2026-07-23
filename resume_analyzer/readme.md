# Resume Analyzer

An AI-powered application that analyzes a resume against a job description using a Large Language Model (LLM). The application identifies matching skills, missing skills, strengths, weaknesses, and provides actionable suggestions to improve the resume for a specific role.

---

## Objective

The goal of this project is to understand how to integrate Large Language Models into real-world applications. Instead of building a chatbot, this project focuses on generating structured and meaningful insights from resumes and job descriptions.

---

## Concepts Learned

### LLM Fundamentals

* What is a Large Language Model (LLM)
* Tokens and context windows
* System, user, and assistant messages
* Prompt engineering
* Temperature and model configuration
* Structured outputs
* JSON response generation
* API integration with an LLM
* Error handling 

### Backend Development

* FastAPI
* REST API development
* Pydantic models
* Request validation
* Response models
* Environment variables
* Exception handling

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Google GenAI
* Uvicorn
* python-dotenv

---

## Features

* Upload or paste a resume
* Submit a job description
* Analyze the resume against the job requirements
* Calculate an estimated match score
* Identify matching skills
* Highlight missing skills
* Suggest improvements
* Return responses in a structured JSON format

---

## Sample Response

```json
{
  "match_score": 82,
  "matching_skills": [
    "Python",
    "FastAPI",
    "REST APIs"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "strengths": [
    "Strong backend development experience",
    "Relevant project work"
  ],
  "recommendations": [
    "Add cloud deployment projects.",
    "Highlight measurable project outcomes."
  ]
}
```




## What I Learned

Building this project helped me understand how LLMs can be integrated into backend applications to solve practical problems. I learned how to design prompts that produce structured outputs, validate AI-generated responses using Pydantic models, and build reliable APIs around LLMs. This project also reinforced the importance of handling API failures, validating inputs, and designing predictable AI-powered services.

---
