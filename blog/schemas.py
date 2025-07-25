from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ResponseBlog(BaseModel):
    title: str
    # body: str

    class Config:
        orm_mode = True
