import os
import json
from types import SimpleNamespace
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
os.environ.pop("OPENAI_API_KEY", None)
from app import main, llm
from app.schemas import StudyResponse


def pack():
    return dict(summary="Summary",key_points=["Point"]*5,flashcards=[dict(q="Question",a="Answer")]*5,quiz=[dict(q="Question",options=["A","B","C","D"],answer_index=0)]*5)


def test_schema():
    p=pack()
    StudyResponse.model_validate(p)
    p["quiz"][0]["answer_index"]=4
    with pytest.raises(ValidationError): StudyResponse.model_validate(p)
    p=pack();p["flashcards"]=[]
    with pytest.raises(ValidationError): StudyResponse.model_validate(p)


def test_routes(monkeypatch):
    with TestClient(main.app) as client:
        assert client.get("/").status_code==200
        for text in ["  ","x"*20001]:
            assert client.post("/study/assist",json={"text":text}).status_code==422
        monkeypatch.setattr(main,"generate_study_pack",lambda **kw:pack())
        for endpoint,keys in [("assist",set(pack()) | {"extra"}),("summary",{"summary","key_points"}),("flashcards",{"flashcards"}),("quiz",{"quiz"})]:
            res=client.post("/study/"+endpoint,json={"text":"Python"})
            assert res.status_code==200
            assert set(res.json())==keys
        def fail(**kw): raise RuntimeError("private configuration")
        monkeypatch.setattr(main,"generate_study_pack",fail)
        res=client.post("/study/assist",json={"text":"Python"})
        assert res.status_code==502
        assert "private" not in res.text


def test_retry_and_missing_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY",raising=False)
    with pytest.raises(RuntimeError):llm.generate_study_pack("Python","en","beginner")
    monkeypatch.setenv("OPENAI_API_KEY","test-only")
    replies=iter(["{}",json.dumps(pack())])
    def create(**kw):return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=next(replies)))])
    monkeypatch.setattr(llm,"OpenAI",lambda **kw:SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))))
    assert llm.generate_study_pack("Python","en","beginner")["summary"]=="Summary"
