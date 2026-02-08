# 🚀 AI Incident Automation System

An AI-powered incident management platform that automatically triages support tickets, predicts severity, analyzes logs, detects root causes, and suggests resolution steps through an interactive dashboard.

---

## 📌 Overview

This project simulates a real-world DevOps/SRE incident automation system.

When a user creates an incident ticket, the system automatically:
- Assigns the appropriate team
- Predicts severity level
- Generates logs
- Detects root cause
- Suggests possible fixes

Built using Python, FastAPI, and Streamlit.

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
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── triage.py
│   ├── severity.py
│   ├── log_analyzer.py
│   ├── llm_engine.py
│
├── frontend/
│   └── app.py

---

## ▶️ How to Run

### Install dependencies
pip install fastapi uvicorn sqlalchemy streamlit requests

### Start backend
cd backend  
python -m uvicorn main:app --reload

### Start frontend (new terminal)
cd frontend  
python -m streamlit run app.py

---

## 🧪 Sample Input

Title: Login failure  
Description: Users unable to login after deployment  
System: Auth  

---

## 💼 Resume Description

Built an AI-powered Incident Automation System using FastAPI and Streamlit that automatically triages incident tickets, predicts severity levels, analyzes logs, detects root causes, and suggests resolution steps.

---

## 🚀 Future Improvements

- ML-based severity prediction  
- User authentication  
- Ticket history analytics  
- Cloud deployment  
- Real LLM integration  

---

## 👩‍💻 Author

Full-stack AI automation project developed using Python, FastAPI, and Streamlit.
