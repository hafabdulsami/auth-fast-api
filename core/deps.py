from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from model.user import UserInDB
from core.config import settings
from database.connection import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        user_data = db.users.find_one({"email": email})
        if not user_data:
            raise credentials_exception
        user = UserInDB(
            id=str(user_data["_id"]),
            email=user_data["email"],
            name=user_data["name"],
            hashedPassword=user_data["hashedPassword"],
        )
    except JWTError:
        raise credentials_exception
    return user