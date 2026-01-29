from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    description:str = ""


fake_db = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    fake_db[item_id] = item
    return {"message": "Item created", "item": item}


@app.get("/items")
def get_all():
    return fake_db


@app.get("/items/{item_id}")
def get_items(item_id:int):
    return fake_db.get(item_id,"Not Found :(")