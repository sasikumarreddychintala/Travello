from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Hostel(Base):
    __tablename__ = "hostels"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    hostel_id = Column(Integer, ForeignKey('hostels.id'))
    type = Column(String)  # "income" or "expense"
    amount = Column(Float)
    date = Column(Date)
    description = Column(String)

class Occupancy(Base):
    __tablename__ = "occupancies"
    id = Column(Integer, primary_key=True)
    hostel_id = Column(Integer, ForeignKey('hostels.id'))
    total_rooms = Column(Integer)
    occupied_rooms = Column(Integer)
    date = Column(Date)

class Complaint(Base):
    __tablename__ = "complaints"
    id = Column(Integer, primary_key=True)
    hostel_id = Column(Integer, ForeignKey('hostels.id'))
    description = Column(String)
    resolved = Column(Boolean)
    date = Column(Date)
