from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, Literal
from datetime import date, datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    role: Literal["viewer", "analyst", "admin"]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str
    date: date
    notes: Optional[str] = None

    @field_validator("category")
    @classmethod
    def category_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Category cannot be empty")
        return value

class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(default=None, gt=0)
    type: Optional[Literal["income", "expense"]] = None
    category: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: Optional[str]
    created_at: datetime
    user_id: int

    model_config = {"from_attributes": True}

class OverviewSummary(BaseModel):
    total_income: float
    total_expenses: float
    balance: float