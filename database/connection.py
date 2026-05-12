from pymongo import MongoClient
from core.config import settings



client = MongoClient(settings.database_url)
db = client[settings.database_name]