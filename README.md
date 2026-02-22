🚀 AI Study Assistant API

A structured AI-powered Study Assistant API built with FastAPI + OpenAI.

This backend transforms any topic or text into:
	•	📘 Summary
	•	🧠 Key Points
	•	🗂 Flashcards
	•	📝 Multiple-choice Quiz

Designed with clean backend architecture and production-ready structure.

⸻

🧠 Features
	•	✅ Structured JSON output (LLM schema controlled)
	•	✅ Strong validation using Pydantic models
	•	✅ Multiple specialized endpoints
	•	✅ Beginner / Intermediate / Advanced explanation levels
	•	✅ Multi-language support (en, de, fa)
	•	✅ Swagger documentation included
	•	✅ Environment variable configuration
	•	✅ Clean error handling with HTTPException

⸻

🏗 Tech Stack
	•	Python 3.13
	•	FastAPI
	•	Pydantic
	•	Uvicorn
	•	OpenAI SDK
	•	python-dotenv
	•	Git

⸻

📂 Project Structure


app/
 ├── main.py
 ├── llm.py
 ├── schemas.py
 └── __init__.py

.env.example
requirements.txt
README.md



⚙️ Setup (Run Locally)

1️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Create Environment File

cp .env.example .env

Then add your OpenAI key inside .env:
OPENAI_API_KEY=your_key_here

4️⃣ Run the Server

uvicorn app.main:app --reload

Server:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs


📡 API Endpoints

🔹 Full Study Pack

POST /study/assist
Returns: summary, key_points, flashcards, quiz, extra

🔹 Summary Only

POST /study/summary
Returns: summary, key_points

🔹 Flashcards Only

POST /study/flashcards
Returns: flashcards

🔹 Quiz Only

POST /study/quiz
Returns: quiz

⸻

📥 Example Request

{
  "text": "Explain REST API in simple terms",
  "language": "en",
  "level": "beginner"
}


📤 Example Response (Shortened)

{
  "summary": "REST is a way to build web services...",
  "key_points": [
    "Uses HTTP methods",
    "Stateless communication"
  ],
  "flashcards": [
    {"q": "What is REST?", "a": "An architectural style for APIs"}
  ],
  "quiz": [
    {
      "q": "Which method creates data?",
      "options": ["GET", "POST", "PUT", "DELETE"],
      "answer_index": 1
    }
  ],
  "extra": null
}


🔐 Environment Variables

Variable
Description
OPENAI_API_KEY
Your OpenAI API key


🎯 Why This Project?

This project demonstrates:
	•	Clean API architecture
	•	Schema validation with Pydantic
	•	Structured LLM output control
	•	Multi-endpoint design
	•	Backend error handling
	•	Environment configuration best practices
	•	Git workflow

⸻

👨‍💻 Author

Hesam Shahbazi
Computer Science Student
AI & Backend Enthusiast
