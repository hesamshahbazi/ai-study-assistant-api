# 🚀 AI Study Assistant API

A structured AI-powered Study Assistant API built with FastAPI and OpenAI.

This backend transforms any topic or text into:

- Summary  
- Key Points  
- Flashcards  
- Multiple-choice Quiz  

Designed with clean backend architecture and production-ready structure.

---

## ✨ Features

- Structured JSON output (LLM schema controlled)
- Strong validation using Pydantic models
- Multiple specialized endpoints
- Beginner / Intermediate / Advanced explanation levels
- Multi-language support (en, de, fa)
- Swagger documentation included
- Environment variable configuration
- Clean error handling

---

## 🏗 Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- OpenAI SDK
- python-dotenv
- Git

---

## 📂 Project Structure

app/  
&nbsp;&nbsp;&nbsp;&nbsp;main.py  
&nbsp;&nbsp;&nbsp;&nbsp;llm.py  
&nbsp;&nbsp;&nbsp;&nbsp;schemas.py  
&nbsp;&nbsp;&nbsp;&nbsp;__init__.py  

.env.example  
requirements.txt  
README.md  

---

## ⚙️ Setup (Run Locally)

1. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

2. Install Dependencies

```
pip install -r requirements.txt
```

3. Create Environment File

```
cp .env.example .env
```

Inside `.env` add:

```
OPENAI_API_KEY=your_key_here
```

4. Run the Server

```
uvicorn app.main:app --reload
```

Server:  
http://localhost:8000  

Swagger UI:  
http://localhost:8000/docs  

---

## 📡 API Endpoints

POST `/study/assist`  
Returns: summary, key_points, flashcards, quiz, extra  

POST `/study/summary`  
Returns: summary, key_points  

POST `/study/flashcards`  
Returns: flashcards  

POST `/study/quiz`  
Returns: quiz  

---

## 🔐 Environment Variables

OPENAI_API_KEY – Your OpenAI API key  

`.env` is ignored by git.

---

## 👨‍💻 Author

Hesam Shahbazi  
Computer Science Student  
AI & Backend Enthusiast