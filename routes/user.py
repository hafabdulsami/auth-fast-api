from services.user import UserService
from fastapi import APIRouter,Depends
from model.user import UserResponse
from core.deps import get_current_user
router = APIRouter(prefix='/users',tags=['users'])

@router.get('/',response_model=list[UserResponse])
def get_users(current_user=Depends(get_current_user), user_service:UserService=Depends()):
    users = user_service.get_all_users()
    return users