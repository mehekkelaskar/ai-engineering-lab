from fastapi import APIRouter
from app.database import db
from app.models.topics import TopicCreate, TopicResponse

router = APIRouter(prefix="/topics", tags=["Topics"])

@router.post("/", response_model=TopicResponse, status_code=201)
def create_topic(topic: TopicCreate):
    new_topic = db.add_topic(topic)
    return new_topic

@router.get("/", response_model=list[TopicResponse])
def get_topics():
    return db.topics_db