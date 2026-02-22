from pydantic import BaseModel, Field
from typing import List, Literal, Optional


Level = Literal["beginner", "intermediate", "advanced"]
Language = Literal["en", "de", "fa"]


class StudyRequest(BaseModel):
    text: str = Field(..., min_length=3, description="User text/topic to study")
    language: Language = Field("fa", description="Output language")
    level: Level = Field("beginner", description="Explanation level")


class Flashcard(BaseModel):
    q: str
    a: str


class QuizQuestion(BaseModel):
    q: str
    options: List[str] = Field(..., min_length=2)
    answer_index: int = Field(..., ge=0, description="Index of correct option in options")


class StudyResponse(BaseModel):
    summary: str
    key_points: List[str]
    flashcards: List[Flashcard]
    quiz: List[QuizQuestion]
    extra: Optional[str] = None

class SummaryOnlyResponse(BaseModel):
    summary: str
    key_points: List[str]


class FlashcardsOnlyResponse(BaseModel):
    flashcards: List[Flashcard]


class QuizOnlyResponse(BaseModel):
    quiz: List[QuizQuestion]