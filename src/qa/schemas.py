from pydantic import BaseModel


class QuizRequest(BaseModel):
    questions_num: int


class QuizResponse(BaseModel):
    questions: list
