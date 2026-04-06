from sqlalchemy.orm import Session
from app import models, schemas

def create_transaction(db: Session, transaction: schemas.TransactionCreate, user_id: int):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        type=transaction.type,
        category=transaction.category,
        date=transaction.date,
        notes=transaction.notes,
        user_id=user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(db: Session, user_id: int, type: str = None, category: str = None, start_date = None, end_date = None):
    query = db.query(models.Transaction).filter(models.Transaction.user_id == user_id)

    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)
    if start_date:
        query = query.filter(models.Transaction.date >= start_date)
    if end_date:
        query = query.filter(models.Transaction.date <= end_date)

    return query.order_by(models.Transaction.date.desc()).all()


def get_transaction_by_id(db: Session, transaction_id: int, user_id: int):
    return db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id,
        models.Transaction.user_id == user_id
    ).first()


def update_transaction(db: Session, db_transaction, transaction_update: schemas.TransactionUpdate):
    for field, value in transaction_update.model_dump(exclude_unset=True).items():
        setattr(db_transaction, field, value)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, db_transaction):
    db.delete(db_transaction)
    db.commit()