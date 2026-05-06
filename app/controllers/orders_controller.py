from typing import List
from app.models.schemas import OrderCreate, OrderResponse
from app.services import orders_service


def create(user_id: int, data: OrderCreate) -> OrderResponse:
    order = orders_service.create_order(user_id, data)
    return OrderResponse(**order)


def get_my_orders(user_id: int) -> List[OrderResponse]:
    orders = orders_service.get_user_orders(user_id)
    return [OrderResponse(**o) for o in orders]
