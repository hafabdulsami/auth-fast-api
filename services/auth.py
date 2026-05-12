from database.connection import db
from model.user import UserCreate, UserInDB
from schema import user
from utils.hashing import hash_password, verify_password
from model.auth import LoginRequest
class AuthService:
    def __init__(self):
        self.db = db

    def create_user(self, user:UserCreate):
        hashed_password_= hash_password(user.password)
        user_data = user.dict()
        user_data.pop("password")
        user_data["hashedPassword"]= hashed_password_
        result = self.db.users.insert_one(user_data)
        created_user = self.db.users.find_one({"_id": result.inserted_id})
        return {
            "id": str(created_user["_id"]),
            "email": created_user["email"],
            "name": created_user["name"]
        }
    
    def login(self,login_credientials:LoginRequest):
        user = self.db.users.find_one({"email": login_credientials.email})
        if user and verify_password(login_credientials.password, user["hashedPassword"]):
            return {
                "email": user["email"],
                "name": user["name"]
            }