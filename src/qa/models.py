from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from src.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, nullable=False)
    answer = Column(String, nullable=False)
    question = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category")
