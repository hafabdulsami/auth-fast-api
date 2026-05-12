from database import db
from model.user import User, UserInDB
from utils.hashing import hash_password
def create_user(user:User):
    print(user)
    hashed_password_= hash_password(user.password)
    user_data = user.dict()
    user_data.pop("password")
    user_data["hashedPassword"]= hashed_password_
    result = db.users.insert_one(user_data)
    return str(result.inserted_id)