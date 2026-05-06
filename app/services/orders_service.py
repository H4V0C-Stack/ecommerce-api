from fastapi import HTTPException, status
from app.models.schemas import OrderCreate
from app.services.products_service import get_product_by_id
from datetime import datetime

orders_db = []
next_order_id = {"value": 1}


def create_order(user_id: int, data: OrderCreate) -> dict:
    order_items = []
    total_price = 0.0

    for item in data.items:
        product = get_product_by_id(item.productId)
        subtotal = round(product["price"] * item.quantity, 2)
        total_price += subtotal
        order_items.append({
            "productId": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    new_order = {
        "id": next_order_id["value"],
        "userId": user_id,
        "items": order_items,
        "totalPrice": round(total_price, 2),
        "status": "nowe",
        "createdAt": datetime.utcnow().isoformat()
    }
    next_order_id["value"] += 1
    orders_db.append(new_order)
    return new_order


def get_user_orders(user_id: int) -> list:
    return [o for o in orders_db if o["userId"] == user_id]
