import json
import os
from openai import OpenAI
from pydantic import ValidationError
from app.schemas import StudyResponse

SYSTEM_PROMPT = """
You are an AI Study Assistant.
Return ONLY valid JSON with keys:
summary (string),
key_points (array of strings),
flashcards (array of {q,a}),
quiz (array of {q, options, answer_index}),
extra (string optional).

Rules:
- key_points: 5 to 10 items.
- flashcards: 5 items.
- quiz: 5 questions, each with 4 options and answer_index between 0..3.
- Language must match the requested language.
- Keep it accurate and beginner-friendly if level=beginner.
"""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_user_prompt(text: str, language: str, level: str) -> str:
    return f"""
Task: Help the user study the topic.
language: {language}
level: {level}

Topic/Text:
{text}
"""


def generate_study_pack(text: str, language: str, level: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Put it in .env file.")

    client = OpenAI(api_key=api_key)

    system_prompt = (
        "You are an AI Study Assistant.\n"
        "Return ONLY valid JSON matching this schema:\n"
        "{\n"
        '  "summary": string,\n'
        '  "key_points": string[],\n'
        '  "flashcards": [{"q": string, "a": string}],\n'
        '  "quiz": [{"q": string, "options": string[], "answer_index": number}],\n'
        '  "extra": string (optional)\n'
        "}\n"
        "Rules:\n"
        "- No extra text outside JSON.\n"
        "- key_points: 5 to 10 items\n"
        "- flashcards: 5 items\n"
        "- quiz: 5 items, each with 4 options, answer_index between 0 and 3\n"
    )

    user_prompt = (
        f"Topic/Text:\n{text}\n\n"
        f"Output language: {language}\n"
        f"Level: {level}\n"
    )

    def _call_llm(extra_instruction: str = "") -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt + (f"\n\n{extra_instruction}" if extra_instruction else "")},
        ]
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            response_format={"type": "json_object"},
        )
        return (resp.choices[0].message.content or "{}").strip()

    # 1) First try
    content = _call_llm()

    # 2) Parse JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # Retry once with a stricter instruction
        content = _call_llm("IMPORTANT: Return ONLY JSON. No markdown, no explanations.")
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            raise RuntimeError("Model returned invalid JSON (could not parse).")

    # 3) Validate schema using Pydantic
    try:
        validated = StudyResponse.model_validate(data)  # pydantic v2
        return validated.model_dump()
    except ValidationError as e:
        # Retry once more with strict fix request
        content = _call_llm(
            "IMPORTANT: Fix your JSON to match the schema exactly. "
            "Ensure quiz has 5 items, each has 4 options, answer_index 0-3. "
            "Return ONLY JSON."
        )
        try:
            data2 = json.loads(content)
            validated2 = StudyResponse.model_validate(data2)
            return validated2.model_dump()
        except Exception:
            raise RuntimeError(f"Model returned JSON but schema validation failed: {str(e)}")
        

    return data