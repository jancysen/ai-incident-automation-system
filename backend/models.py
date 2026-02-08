from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    system = Column(String)
    severity = Column(String)
    assigned_team = Column(String)
    status = Column(String, default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    log_text = Column(String)
    root_cause = Column(String)


class Suggestion(Base):
    __tablename__ = "suggestions"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    suggestion_text = Column(String)
