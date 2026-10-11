from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated

StudyText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length=20000)]
NonBlank = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
from typing import List, Literal, Optional


Level = Literal["beginner", "intermediate", "advanced"]
Language = Literal["en", "de", "fa"]


class StudyRequest(BaseModel):
    text: StudyText = Field(..., description="User text/topic to study")
    language: Language = Field("fa", description="Output language")
    level: Level = Field("beginner", description="Explanation level")


class Flashcard(BaseModel):
    q: NonBlank
    a: NonBlank


class QuizQuestion(BaseModel):
    q: NonBlank
    options: List[NonBlank] = Field(..., min_length=4, max_length=4)
    answer_index: int = Field(..., ge=0, le=3, description="Index of correct option in options")


class StudyResponse(BaseModel):
    summary: NonBlank
    key_points: List[NonBlank] = Field(..., min_length=5, max_length=10)
    flashcards: List[Flashcard] = Field(..., min_length=5, max_length=5)
    quiz: List[QuizQuestion] = Field(..., min_length=5, max_length=5)
    extra: Optional[str] = None

class SummaryOnlyResponse(BaseModel):
    summary: NonBlank
    key_points: List[NonBlank] = Field(..., min_length=5, max_length=10)


class FlashcardsOnlyResponse(BaseModel):
    flashcards: List[Flashcard] = Field(..., min_length=5, max_length=5)


class QuizOnlyResponse(BaseModel):
    quiz: List[QuizQuestion] = Field(..., min_length=5, max_length=5)