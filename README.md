# 🚀 AI Study Assistant API

A structured **FastAPI** backend powered by **OpenAI** that transforms any text or topic into a complete study pack:

- Summary  
- Key Points  
- Flashcards  
- Multiple Choice Quiz  

Built with clean architecture, strict Pydantic validation, and interactive API documentation.

---

## ✨ Features

- Structured JSON output (LLM schema controlled)
- Multiple output modes:
  - Full Study Pack
  - Summary Only
  - Flashcards Only
  - Quiz Only
- Language support: English, German, Persian
- Level support: beginner / intermediate / advanced
- Clean HTTP error handling
- Interactive Swagger documentation

---

## 🧰 Tech Stack

- Python 3.x
- FastAPI
- Pydantic
- Uvicorn
- OpenAI SDK
- python-dotenv
- Git

---

## 🗂 Project Structure

ai-study-assistant-api/  
├─ app/  
│  ├─ __init__.py  
│  ├─ main.py  
│  ├─ schemas.py  
│  └─ llm.py  
├─ requirements.txt  
├─ .env.example  
├─ README.md  
└─ .gitignore  

---

## ⚙️ Setup (Run Locally)

### 1. Create & activate virtual environment

python3 -m venv venv  
source venv/bin/activate  

### 2. Install dependencies

pip install -r requirements.txt  

### 3. Create environment file

cp .env.example .env  

Inside `.env` add:

OPENAI_API_KEY=YOUR_KEY_HERE  

### 4. Run the server

uvicorn app.main:app --reload  

Server:  
http://localhost:8000  

Swagger UI:  
http://localhost:8000/docs  

---

## 🔌 API Endpoints

POST /study/assist  
Returns: summary, key_points, flashcards, quiz, extra  

POST /study/summary  
Returns: summary, key_points  

POST /study/flashcards  
Returns: flashcards  

POST /study/quiz  
Returns: quiz  

---

## 📨 Example Request

{
  "text": "Explain REST APIs in simple terms",
  "language": "en",
  "level": "beginner"
}

---

## 🎯 Why This Project?

This project demonstrates:

- Clean backend API architecture
- Schema validation with Pydantic
- Structured LLM output control
- Multi-endpoint API design
- External AI service integration
- Production-ready backend practices

---

## 👤 Author

Hesam Shahbazi  
Computer Science Student  
Backend & AI Enthusiast