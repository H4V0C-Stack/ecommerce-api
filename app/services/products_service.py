from fastapi import HTTPException, status
from app.models.schemas import ProductCreate, ProductUpdate

# Baza produktów w pamięci
products_db = [
    {"id": 1, "name": "Laptop Dell XPS 15", "price": 5999.99, "category": "laptopy", "stock": 10},
    {"id": 2, "name": "iPhone 15 Pro", "price": 4999.99, "category": "telefony", "stock": 25},
    {"id": 3, "name": "Sony WH-1000XM5", "price": 1299.99, "category": "sluchawki", "stock": 50},
]
next_id = {"value": 4}


def get_all_products() -> list:
    return products_db


def get_product_by_id(product_id: int) -> dict:
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produkt nie został znaleziony"
        )
    return product


def create_product(data: ProductCreate) -> dict:
    new_product = {
        "id": next_id["value"],
        "name": data.name,
        "price": data.price,
        "category": data.category,
        "stock": data.stock
    }
    next_id["value"] += 1
    products_db.append(new_product)
    return new_product


def update_product(product_id: int, data: ProductUpdate) -> dict:
    product = get_product_by_id(product_id)
    if data.name is not None:
        product["name"] = data.name
    if data.price is not None:
        product["price"] = round(data.price, 2)
    if data.category is not None:
        product["category"] = data.category
    if data.stock is not None:
        product["stock"] = data.stock
    return product


def delete_product(product_id: int) -> dict:
    product = get_product_by_id(product_id)
    products_db.remove(product)
    return {"message": "Produkt został usunięty"}
