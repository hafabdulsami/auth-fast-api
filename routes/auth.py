from services.auth import AuthService
from fastapi import APIRouter,Depends
from model.user import UserCreate,UserResponse
from model.auth import LoginRequest,LoginResponse
router =APIRouter(prefix='/auth',tags=['auth'])

@router.post('/register',response_model=UserResponse)
def register(user:UserCreate,auth_service:AuthService=Depends()):
    user = auth_service.create_user(user)
    return user

@router.post('/login',response_model=LoginResponse)
def login(request:LoginRequest,auth_service:AuthService=Depends()):
    user = auth_service.login(request)
    return user