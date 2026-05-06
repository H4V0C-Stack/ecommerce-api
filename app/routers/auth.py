from fastapi import APIRouter
from app.models.schemas import UserRegister, UserLogin, UserResponse, TokenResponse
from app.controllers import auth_controller

router = APIRouter(prefix="/auth", tags=["Autoryzacja"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserRegister):
    return auth_controller.register(data)


@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin):
    return auth_controller.login(data)
