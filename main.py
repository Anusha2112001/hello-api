
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Hello API",
    description="A simple API for learning GitHub integration",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def home():
    return {"message": "Welcome to Hello API"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {
    "message": f"Welcome, {name}!",
    "name": name,
    "status": "success"
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created",
        "item": item
    }