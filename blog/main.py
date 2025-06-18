from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import Optional, List
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blogs(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blogs", response_model=List[schemas.ResponseBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def getById(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} is not found"
        )
    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} is not found"
        )
    db.delete(blog)
    db.commit()
    # return {"message:" f"The deletion for the id {id} has been done"}

    return {f"The deletion for the id {id} has been done"}


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(request: schemas.Blog, id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    blog.update(request.model_dump())
    db.commit()
    return "This is completed"
