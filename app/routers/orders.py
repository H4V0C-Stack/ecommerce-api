from typing import List
from fastapi import APIRouter, Depends
from app.models.schemas import OrderCreate, OrderResponse
from app.controllers import orders_controller
from app.middleware.auth_middleware import get_current_user

router = APIRouter(prefix="/orders", tags=["Zamówienia"])


@router.post("/", response_model=OrderResponse, status_code=201)
def create(data: OrderCreate, current_user=Depends(get_current_user)):
    return orders_controller.create(current_user["id"], data)


@router.get("/", response_model=List[OrderResponse])
def get_my_orders(current_user=Depends(get_current_user)):
    return orders_controller.get_my_orders(current_user["id"])
