from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models

def get_overview_summary(db: Session, user_id: int):
    total_income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == "income"
    ).scalar() or 0

    total_expenses = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == "expense"
    ).scalar() or 0

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": total_income - total_expenses
    }


def get_category_breakdown(db: Session, user_id: int):
    results = db.query(
        models.Transaction.category,
        func.sum(models.Transaction.amount)
    ).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == "expense"
    ).group_by(models.Transaction.category).all()

    return [{"category": category, "total": total} for category, total in results]


def get_recent_activity(db: Session, user_id: int):
    return db.query(models.Transaction).filter(
        models.Transaction.user_id == user_id
    ).order_by(models.Transaction.created_at.desc()).limit(5).all()


def get_monthly_summary(db: Session, user_id: int):
    results = db.query(
        func.strftime("%Y-%m", models.Transaction.date).label("month"),
        models.Transaction.type,
        func.sum(models.Transaction.amount)
    ).filter(
        models.Transaction.user_id == user_id
    ).group_by("month", models.Transaction.type).all()

    monthly_data = {}
    for month, txn_type, total in results:
        if month not in monthly_data:
            monthly_data[month] = {"month": month, "income": 0, "expense": 0}
        monthly_data[month][txn_type] = total

    return list(monthly_data.values())