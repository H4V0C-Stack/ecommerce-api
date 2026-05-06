from typing import List
from fastapi import APIRouter, Depends
from app.models.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.controllers import products_controller
from app.middleware.auth_middleware import get_current_user

router = APIRouter(prefix="/products", tags=["Produkty"])


@router.get("/", response_model=List[ProductResponse])
def get_all():
    return products_controller.get_all()


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(product_id: int):
    return products_controller.get_by_id(product_id)


@router.post("/", response_model=ProductResponse, status_code=201)
def create(data: ProductCreate, current_user=Depends(get_current_user)):
    return products_controller.create(data)


@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, data: ProductUpdate, current_user=Depends(get_current_user)):
    return products_controller.update(product_id, data)


@router.delete("/{product_id}")
def delete(product_id: int, current_user=Depends(get_current_user)):
    return products_controller.delete(product_id)
