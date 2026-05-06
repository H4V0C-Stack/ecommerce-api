from fastapi import HTTPException
from app.models.schemas import UserRegister, UserLogin, UserResponse, TokenResponse
from app.services import auth_service


def register(data: UserRegister) -> UserResponse:
    result = auth_service.register_user(data.email, data.password)
    return UserResponse(**result)


def login(data: UserLogin) -> TokenResponse:
    result = auth_service.login_user(data.email, data.password)
    return TokenResponse(**result)
