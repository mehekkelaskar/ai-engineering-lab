from pydantic import BaseModel

class TopicCreate(BaseModel):
    name: str
    description: str

class TopicResponse(BaseModel):
    id: int
    name: str
    description: str