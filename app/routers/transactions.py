from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import List, Optional

from app import schemas
from app.dependencies import get_db, get_current_user
from app.core.roles import require_roles
from app.services import transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=schemas.TransactionResponse, status_code=201)
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    require_roles(current_user.role, ["admin"])
    return transaction_service.create_transaction(db, transaction, current_user.id)


@router.get("/", response_model=List[schemas.TransactionResponse])
def get_transactions(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    require_roles(current_user.role, ["viewer", "analyst", "admin"])
    return transaction_service.get_transactions(db, current_user.id, type, category, start_date, end_date)


@router.get("/{transaction_id}", response_model=schemas.TransactionResponse)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    require_roles(current_user.role, ["viewer", "analyst", "admin"])
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, current_user.id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction


@router.put("/{transaction_id}", response_model=schemas.TransactionResponse)
def update_transaction(
    transaction_id: int,
    transaction_update: schemas.TransactionUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    require_roles(current_user.role, ["admin"])
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, current_user.id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction_service.update_transaction(db, transaction, transaction_update)


@router.delete("/{transaction_id}", status_code=200)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    require_roles(current_user.role, ["admin"])
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, current_user.id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    transaction_service.delete_transaction(db, transaction)
    return {"message": "Transaction deleted successfully"}