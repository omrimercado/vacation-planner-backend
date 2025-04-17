from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Trip(Base):
    __tablename__ = "trips"

    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, index=True, nullable=False)
    destination = Column(String, nullable=False)
    start_date  = Column(Date,   nullable=False)
    end_date    = Column(Date,   nullable=False)