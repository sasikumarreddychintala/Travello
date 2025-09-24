from pydantic import BaseModel
from datetime import date
from typing import List

class ReportResponse(BaseModel):
    total_income: float
    total_expense: float
    occupancy_rate: float
    complaints_resolved: int
    total_complaints: int
