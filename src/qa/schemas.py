from pydantic import BaseModel
from datetime import datetime


class QuizRequest(BaseModel):
    questions_num: int


class QuizResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
