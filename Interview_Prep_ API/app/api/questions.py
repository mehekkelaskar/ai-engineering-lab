from fastapi import APIRouter, HTTPException, status
from app.database import db
from app.models.questions import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=QuestionResponse, status_code=201)
def create_question(question: QuestionCreate):
    # Verify the referenced topic folder actually exists first
    topic_exists = any(t["id"] == question.topic_id for t in db.topics_db)
    if not topic_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Topic with ID {question.topic_id} does not exist."
        )
    return db.add_question(question.dict())

@router.get("/", response_model=list[QuestionResponse])
def get_questions(technology: str = None, difficulty: str = None):
    return db.get_all_questions(technology=technology, difficulty=difficulty)

@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int):
    question = db.get_question_by_id(question_id)
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Question not found."
        )
    return question

@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(question_id: int, updated_question: QuestionCreate):
    updated = db.update_question_by_id(question_id, updated_question.dict())
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Question not found."
        )
    return updated

@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int):
    success = db.delete_question_by_id(question_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Question not found."
        )
    # 204 No Content responses return empty body structures
    return None