import requests
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .schemas import QuizRequest, QuizResponse
from .models import Question, Category
from src.database import get_db

router = APIRouter()


@router.post("/get_questions/", status_code=status.HTTP_201_CREATED, response_model=List[QuizResponse])
async def get_questions(quiz_request: QuizRequest, db: AsyncSession = Depends(get_db), ):
    questions_num = quiz_request.questions_num
    if questions_num <= 0:
        raise HTTPException(status_code=400, detail="Invalid questions_num. Must be a positive integer.")

    filtered_questions = []
    while len(filtered_questions) < questions_num:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num - len(filtered_questions)}")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch quiz questions from the API.")

        questions = response.json()

        for q in questions:
            cat_id = q['category']['id']
            query = select(Category).filter(Category.id == cat_id)
            result = await db.execute(query)
            existing_category = result.scalar()
            if existing_category is None:
                category = Category(
                    id=cat_id,
                    title=q['category']['title'],
                    created_at=datetime.strptime(q['category']['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    updated_at=datetime.strptime(q['category']['updated_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                )
                db.add(category)

            question_id = q['id']
            query = select(Question).filter(Question.id == question_id)
            result = await db.execute(query)
            existing_question = result.scalar()
            if existing_question is None:
                question = Question(
                    id=question_id,
                    answer=q['answer'],
                    question=q['question'],
                    created_at=datetime.strptime(q['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    updated_at=datetime.strptime(q['updated_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                    category_id=cat_id
                )
                db.add(question)
                await db.commit()
                filtered_questions.append(
                    QuizResponse(
                        id=question_id,
                        question=q['question'],
                        answer=q['answer'],
                        created_at=q.get('created_at')
                    )
                )

    return filtered_questions
