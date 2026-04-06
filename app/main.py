from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, transactions, summary

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinTrack API",
    description="A role-based personal finance tracking backend built with FastAPI",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(summary.router)


@app.get("/")
def root() -> dict:
    return {
        "message": "Welcome Team Zorvyn! Thank you for reviewing my FinTrack API assignment.",
        "project": "FinTrack API - Personal Finance Tracking Backend",
        "docs": "Visit /docs for API documentation",
        "status": "API is running successfully"
    }