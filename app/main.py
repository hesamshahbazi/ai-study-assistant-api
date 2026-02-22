from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

from app.schemas import (
    StudyRequest,
    StudyResponse,
    SummaryOnlyResponse,
    FlashcardsOnlyResponse,
    QuizOnlyResponse,
)
from app.llm import generate_study_pack

app = FastAPI(title="AI Study Assistant API")


@app.get("/")
def root():
    return {"message": "AI Study Assistant is running"}


@app.post("/study/assist", response_model=StudyResponse)
def study_assist(request: StudyRequest):
    try:
        return generate_study_pack(
            text=request.text,
            language=request.language,
            level=request.level,
        )
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@app.post("/study/summary", response_model=SummaryOnlyResponse)
def study_summary(request: StudyRequest):
    try:
        data = generate_study_pack(
            text=request.text,
            language=request.language,
            level=request.level,
        )
        return {"summary": data["summary"], "key_points": data["key_points"]}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@app.post("/study/flashcards", response_model=FlashcardsOnlyResponse)
def study_flashcards(request: StudyRequest):
    try:
        data = generate_study_pack(
            text=request.text,
            language=request.language,
            level=request.level,
        )
        return {"flashcards": data["flashcards"]}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@app.post("/study/quiz", response_model=QuizOnlyResponse)
def study_quiz(request: StudyRequest):
    try:
        data = generate_study_pack(
            text=request.text,
            language=request.language,
            level=request.level,
        )
        return {"quiz": data["quiz"]}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")