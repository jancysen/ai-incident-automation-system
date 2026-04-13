# 🚀 AI Incident Automation System

An AI-powered incident management platform that automatically triages support tickets, predicts severity, analyzes logs, detects root causes, and suggests resolution steps through an interactive dashboard.

---

## 📌 Overview

This project simulates a real-world **DevOps/SRE incident automation system**.

When a user creates an incident ticket, the system automatically:

- Assigns the appropriate team  
- Predicts severity level  
- Generates logs  
- Detects root cause  
- Suggests possible fixes  

Built using **Python, FastAPI, and Streamlit**, this system demonstrates how AI can enhance incident response workflows.

---

## 🌍 Real-World Use Case

Modern DevOps and SRE teams deal with thousands of incidents daily. Manual triaging is time-consuming and error-prone.

This system:
- Reduces manual effort  
- Speeds up incident resolution  
- Improves system reliability  
- Mimics real-world production workflows  

---

## ⭐ Key Highlights

- End-to-end AI system with backend + frontend integration  
- Simulates real-world DevOps automation workflows  
- Modular and scalable architecture  
- Combines rule-based + AI-inspired logic  

---

## 🎯 Features

- 🧾 Ticket creation from dashboard  
- 🤖 Automatic team assignment  
- 🚨 Severity prediction (Critical / High / Medium / Low)  
- 📜 Log generation  
- 🔍 Root cause detection  
- 💡 AI-style resolution suggestions  
- 📊 Interactive Streamlit UI  

---

## 🏗 Architecture

**Frontend:** Streamlit  
**Backend:** FastAPI  
**Database:** SQLite  
**AI Modules:**  
- Severity prediction  
- Log analysis  
- Root cause detection  

### Flow:
User Input → FastAPI Backend → AI Processing → Database → Results → Streamlit Dashboard

---

## 📸 Demo / Output

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/b5d50a2b-00ba-4f1a-81de-60b57231c3c0" />


Example:
- Dashboard UI  
- Ticket creation screen  
- Output predictions  

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Streamlit  

---

## 📂 Project Structure
AI-Incident-Automation-System/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── triage.py
│ ├── severity.py
│ ├── log_analyzer.py
│ ├── llm_engine.py
│
├── frontend/
│ └── app.py

---

## ▶️ How to Run

### 1. Clone the repository
git clone <your-repo-link>
cd AI-Incident-Automation-System


### 2. Install dependencies

pip install fastapi uvicorn sqlalchemy streamlit requests


### 3. Start backend

cd backend
uvicorn main:app --reload


### 4. Start frontend (new terminal)

cd frontend
streamlit run app.py

---

## 🧪 Sample Input

- **Title:** Login failure  
- **Description:** Users unable to login after deployment  
- **System:** Auth  

---

## 💼 Resume Description

Built an AI-powered Incident Automation System using FastAPI and Streamlit that automatically triages incident tickets, predicts severity levels, analyzes logs, detects root causes, and suggests resolution steps.

---

## 🚀 Future Improvements

- ML-based severity prediction  
- User authentication system  
- Ticket history analytics  
- Cloud deployment (AWS/GCP)  
- Real LLM integration  

---

## 👩‍💻 Author

Developed by **Jancy S**  
Final-year engineering student passionate about AI, ML, and real-world system design.

---

## 📢 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
