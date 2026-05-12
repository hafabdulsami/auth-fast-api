from database.connection import db

class UserService:
    def __init__(self):
        self.db = db

    def get_user_by_email(self,email:str):
        user = self.db.users.find_one({"email": email})
        if user:
            return {
                "id": str(user["_id"]),
                "email": user["email"],
                "name": user["name"]
            }

    def get_all_users(self):
        users = self.db.users.find()
        return [
            {
                "id": str(user["_id"]),
                "email": user["email"],
                "name": user["name"]
            }
            for user in users
        ]  