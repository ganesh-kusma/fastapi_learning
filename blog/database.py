from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = "sqlite:///./blogs.db"

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)  # create engine

Base = declarative_base()  # create declarative base
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False
)  # create session
