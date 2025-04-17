from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.trip import TripCreate, TripRead
from app.models.trip import Trip
from app.db.deps import get_db
from typing import List
router = APIRouter()  # <-- must be named "router"

@router.post("/", response_model=TripRead, status_code=status.HTTP_201_CREATED)
def create_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    trip = Trip(**trip_in.dict())
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

@router.get("/{trip_id}", response_model=TripRead)
def read_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.get(Trip, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip
@router.get("/", response_model=List[TripRead], summary="List all trips")
def list_trips(db: Session = Depends(get_db)):
    return db.query(Trip).all()