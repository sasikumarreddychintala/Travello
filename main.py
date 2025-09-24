from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import ReportResponse
from crud import generate_hostel_report
from datetime import date

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/hostel/{hostel_id}/report", response_model=ReportResponse)
def hostel_report(hostel_id: int, start_date: date, end_date: date, db: Session = Depends(get_db)):
    report = generate_hostel_report(db, hostel_id, start_date, end_date)
    return report
