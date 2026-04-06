from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.core.roles import require_roles
from app.services import summary_service
from app import schemas

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.get("/overview", response_model=schemas.OverviewSummary)
def overview(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_roles(current_user.role, ["viewer", "analyst", "admin"])
    return summary_service.get_overview_summary(db, current_user.id)


@router.get("/category-breakdown")
def category_breakdown(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_roles(current_user.role, ["analyst", "admin"])
    return summary_service.get_category_breakdown(db, current_user.id)


@router.get("/recent")
def recent_activity(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_roles(current_user.role, ["viewer", "analyst", "admin"])
    return summary_service.get_recent_activity(db, current_user.id)


@router.get("/monthly")
def monthly_summary(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_roles(current_user.role, ["analyst", "admin"])
    return summary_service.get_monthly_summary(db, current_user.id)