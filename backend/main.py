from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from pydantic import BaseModel

from triage import assign_team
from severity import predict_severity
from log_analyzer import generate_logs, find_root_cause
from llm_engine import get_ai_suggestion

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Incident Automation System Running"}

class TicketCreate(BaseModel):
    title: str
    description: str
    system: str

@app.post("/create-ticket")
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):

    # Assign team + severity
    team = assign_team(ticket.description)
    severity = predict_severity(ticket.description)

    # Save ticket
    new_ticket = models.Ticket(
        title=ticket.title,
        description=ticket.description,
        system=ticket.system,
        severity=severity,
        assigned_team=team
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    # Generate logs
    log_text = generate_logs(ticket.description)
    root_cause = find_root_cause(log_text)

    new_log = models.Log(
        ticket_id=new_ticket.id,
        log_text=log_text,
        root_cause=root_cause
    )

    db.add(new_log)
    db.commit()

    # 🤖 AI suggestion
    ai_suggestion = get_ai_suggestion(
        ticket.title,
        ticket.description,
        log_text,
        root_cause
    )

    new_suggestion = models.Suggestion(
        ticket_id=new_ticket.id,
        suggestion_text=ai_suggestion
    )

    db.add(new_suggestion)
    db.commit()

    return {
        "message": "Ticket created successfully",
        "ticket_id": new_ticket.id,
        "assigned_team": team,
        "severity": severity,
        "log": log_text,
        "root_cause": root_cause,
        "ai_suggestion": ai_suggestion
    }
