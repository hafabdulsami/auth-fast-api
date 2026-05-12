from services.auth import AuthService
from fastapi import APIRouter,Depends
from model.user import UserCreate,UserResponse

router =APIRouter(prefix='/auth',tags=['auth'])

@router.post('/register',response_model=UserResponse)
def register(user:UserCreate,auth_service:AuthService=Depends()):
    user = auth_service.create_user(user)
    return user