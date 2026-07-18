# Interview Question API

A RESTful API built using **FastAPI** to manage interview questions categorized by technology and difficulty. This project focuses on understanding the fundamentals of API development using FastAPI while following clean backend development practices.

---

## Objective

The primary goal of this project is to learn the core concepts of FastAPI by building a simple CRUD application. Instead of only studying the framework, this project applies each concept through practical implementation.

---

## Concepts Learned

* FastAPI project setup
* Creating API routes
* HTTP methods (GET, POST, PUT, DELETE)
* Path parameters
* Query parameters
* Request bodies
* Pydantic models
* Request validation
* Response models
* HTTP status codes
* Interactive API documentation (Swagger UI & ReDoc)

---

## Technologies Used

* Python 3
* FastAPI
* Uvicorn
* Pydantic

---

## Features

* Add a new interview question
* Retrieve all interview questions
* Retrieve a question by ID
* Update an existing question
* Delete a question
* Filter questions by technology
* Filter questions by difficulty


## Project Structure

```text
interview_prep_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # App initialization & entry point
│   │
│   ├── api/                     # All API route definitions
│   │   ├── __init__.py
│   │   ├── topics.py            # /topics endpoints
│   │   └── questions.py         # /questions endpoints
│   │
│   ├── models/                  # Pydantic schemas for request/response validation
│   │   ├── __init__.py
│   │   ├── topics.py            # Topic Pydantic models
│   │   └── questions.py         # Question Pydantic models
│   │
│   └── database.py              # In-memory mock database (lists/dicts)
│
├── .gitignore
├── README.md
└── requirements.txt
```



---

## What I Learned

Through this project, I learned how FastAPI simplifies backend API development while providing automatic request validation and interactive API documentation. I also understood how Pydantic models help validate incoming data and how different HTTP methods are used to perform CRUD operations. Building this project strengthened my understanding of designing REST APIs and organizing backend code for maintainability.

---

## Future Improvements

* Integrate PostgreSQL for persistent data storage
* Add SQLAlchemy ORM
* Implement JWT authentication
* Introduce pagination
* Add API testing using Pytest
* Deploy the API using Docker

---

## Learning Outcome

After completing this project, I am comfortable with the core FastAPI concepts required to build basic REST APIs. This serves as the foundation for more advanced backend development topics such as database integration, authentication, dependency injection, and AI-powered APIs in the upcoming phases.
