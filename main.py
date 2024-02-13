from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world!"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None):   # or -> q: str | None = None
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/items")
async def read_items(q: str = Query(..., min_length=2, max_length=10)):
    results = {"items": [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
