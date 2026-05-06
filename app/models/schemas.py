from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Optional
from datetime import datetime


# ── AUTH ──────────────────────────────────────────────────────────────────

class UserRegister(BaseModel):
    email: str
    password: str

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, v):
        if '@' not in v or '.' not in v.split('@')[-1]:
            raise ValueError('Nieprawidłowy format email')
        return v.lower()

    @field_validator('password')
    @classmethod
    def password_min_length(cls, v):
        if len(v) < 6:
            raise ValueError('Hasło musi mieć minimum 6 znaków')
        return v


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str


class TokenResponse(BaseModel):
    token: str
    token_type: str = "bearer"


# ── PRODUCTS ──────────────────────────────────────────────────────────────

class ProductCreate(BaseModel):
    name: str
    price: float
    category: str
    stock: int = 0

    @field_validator('name')
    @classmethod
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Nazwa produktu nie może być pusta')
        return v

    @field_validator('price')
    @classmethod
    def price_positive(cls, v):
        if v <= 0:
            raise ValueError('Cena musi być większa niż 0')
        return round(v, 2)

    @field_validator('stock')
    @classmethod
    def stock_non_negative(cls, v):
        if v < 0:
            raise ValueError('Stan magazynowy nie może być ujemny')
        return v


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    stock: Optional[int] = None

    @field_validator('price')
    @classmethod
    def price_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Cena musi być większa niż 0')
        return v


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    stock: int


# ── ORDERS ────────────────────────────────────────────────────────────────

class OrderItem(BaseModel):
    productId: int
    quantity: int

    @field_validator('quantity')
    @classmethod
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError('Ilość musi być większa niż 0')
        return v


class OrderItemResponse(BaseModel):
    productId: int
    name: str
    price: float
    quantity: int
    subtotal: float


class OrderCreate(BaseModel):
    items: List[OrderItem]

    @field_validator('items')
    @classmethod
    def items_not_empty(cls, v):
        if not v:
            raise ValueError('Zamówienie musi zawierać przynajmniej jeden produkt')
        return v


class OrderResponse(BaseModel):
    id: int
    userId: int
    items: List[OrderItemResponse]
    totalPrice: float
    status: str
    createdAt: str
