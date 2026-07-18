from pydantic import BaseModel

class QuestionCreate(BaseModel):
    topic_id: int
    question_text: str
    answer_text: str
    difficulty: str  # e.g., "easy", "medium", "hard"
    technology: str  # e.g., "java", "python"

class QuestionResponse(BaseModel):
    id: int
    topic_id: int
    question_text: str
    answer_text: str
    difficulty: str
    technology: str