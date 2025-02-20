from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__: str = "products"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String, index=True)
    description: Column[str] = Column(String, nullable=True)
    price: Column[float] = Column(Float)
    stock: Column[int] = Column(Integer)
    discount: Column[int] = Column(Integer)
