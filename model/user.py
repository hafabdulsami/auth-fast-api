from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    name:str
    
class UserResponse(BaseModel):
    id:str
    email:EmailStr
    name:str

class UserInDB(UserResponse):
    name:str
    email:EmailStr
    hashedPassword:str
