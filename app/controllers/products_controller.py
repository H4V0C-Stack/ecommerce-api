from typing import List
from app.models.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.services import products_service


def get_all() -> List[ProductResponse]:
    products = products_service.get_all_products()
    return [ProductResponse(**p) for p in products]


def get_by_id(product_id: int) -> ProductResponse:
    product = products_service.get_product_by_id(product_id)
    return ProductResponse(**product)


def create(data: ProductCreate) -> ProductResponse:
    product = products_service.create_product(data)
    return ProductResponse(**product)


def update(product_id: int, data: ProductUpdate) -> ProductResponse:
    product = products_service.update_product(product_id, data)
    return ProductResponse(**product)


def delete(product_id: int) -> dict:
    return products_service.delete_product(product_id)
