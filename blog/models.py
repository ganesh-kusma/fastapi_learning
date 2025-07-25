from sqlalchemy import Column, Integer, String
from .database import Base


class Blogs(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
