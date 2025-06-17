from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index(limit, published: Optional[bool] = False):
    return {"data": {"name": f"Ganesh {limit} {published}"}}


@app.get("/{id}")
def index(id: int):
    return {"data": {"id": id, "name": "id-page"}}


@app.get("/about")
def index():
    return {"data": {"name": "about page"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False


@app.post("/blog")
def post(request: Blog):
    return {
        f"posted the data successfully {request.title} {request.body} {request.published}"
    }
