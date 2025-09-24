from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Transaction, Occupancy, Complaint

def generate_hostel_report(db: Session, hostel_id: int, start_date: date, end_date: date):
    income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.hostel_id == hostel_id,
        Transaction.type == 'income',
        Transaction.date.between(start_date, end_date)
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.amount)).filter(
        Transaction.hostel_id == hostel_id,
        Transaction.type == 'expense',
        Transaction.date.between(start_date, end_date)
    ).scalar() or 0

    occupancy_entry = db.query(Occupancy).filter(
        Occupancy.hostel_id == hostel_id,
        Occupancy.date.between(start_date, end_date)
    ).order_by(Occupancy.date.desc()).first()

    occupancy_rate = (
        (occupancy_entry.occupied_rooms / occupancy_entry.total_rooms) * 100
        if occupancy_entry else 0
    )

    total_complaints = db.query(Complaint).filter(
        Complaint.hostel_id == hostel_id,
        Complaint.date.between(start_date, end_date)
    ).count()

    resolved_complaints = db.query(Complaint).filter(
        Complaint.hostel_id == hostel_id,
        Complaint.date.between(start_date, end_date),
        Complaint.resolved == True
    ).count()

    return {
        "total_income": income,
        "total_expense": expense,
        "occupancy_rate": occupancy_rate,
        "complaints_resolved": resolved_complaints,
        "total_complaints": total_complaints
    }
