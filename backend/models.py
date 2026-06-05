from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    cover = Column(String, nullable=True)
    publisher = Column(String, nullable=False)
    category = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

    is_available = Column(Boolean, default=True)
    is_favorite = Column(Boolean, default=False)
    is_reserved = Column(Boolean, default=False)
    collection = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)