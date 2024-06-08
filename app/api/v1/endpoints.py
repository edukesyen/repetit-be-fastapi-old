from typing import Union, Any
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.quiz.quiz_scheduler import QuizScheduler


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.post("/quiz-scheduler", response_model=None)
async def get_next_quiz_schedule(
    db = None,
    user_id = None,
    course_id = None,
    Topic_id = None,
    quiz_id = None,
) -> Any:
    quiz_scheduler = QuizScheduler()
    # quiz_detail = None 
    # topic_detail = None
    # course_detail = None
    response = {
        "quizId": 0,
        "topicId": 0,
        "topicName": "Linked List",
        "courseId":0,
        "courseName": "Struktur Data",
        "reviewDate": quiz_scheduler.get_review_date()
    }
    return JSONResponse(status_code=200, content=jsonable_encoder(response))