import requests
from typing import List
from fastapi import APIRouter, HTTPException

from .schemas import QuizRequest, QuizResponse

router = APIRouter()


@router.post("/get_questions/", response_model=List[QuizResponse])
async def get_questions(quiz_request: QuizRequest):
    questions_num = quiz_request.questions_num
    if questions_num <= 0:
        raise HTTPException(status_code=400, detail="Invalid questions_num. Must be a positive integer.")

    response = requests.get(f"https://jservice.io/api/random?count={questions_num}")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch quiz questions from the API.")

    questions = response.json()

    filtered_questions = [
        QuizResponse(
            id=q['id'],
            question=q['question'],
            answer=q['answer'],
            created_at=q.get('created_at')
        )
        for q in questions
    ]

    return filtered_questions
