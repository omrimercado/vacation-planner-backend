# app/main.py
from fastapi import FastAPI
from app.routers.users import router as users_router

# import these so we can create tables
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Vacation Planner API")

# automatically create all tables on app startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/health", summary="Health check")
async def health_check():
    return {"status": "ok"}
