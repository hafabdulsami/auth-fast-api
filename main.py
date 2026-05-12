from fastapi import FastAPI
from model.item import Item
from core.config import settings
from routes.auth import router as auth_router
app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/item/{item_id}")
def get_item(item_id:int):
    return {"item_id":item_id}

@app.get("/items/{item_id}")
def update_item(item_id:int,item:Item):
    print(settings)
    return{"item_id":item_id,"item":item}