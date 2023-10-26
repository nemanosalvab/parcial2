from typing import Union
import json
from fastapi import FastAPI

app = FastAPI()
pregrados_unal= open('./programas.json', encoding='utf-8')
data = json.load(pregrados_unal)

@app.get("/")
def read_root():
    return {item['Código SNIES']: item for item in data}
    #return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}