from pydantic import BaseModel, field_validator
from typing import Optional

class ProductBaseDTO(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    discount: Optional[int] = None
    priceDiscount: Optional[float] = None

    @field_validator("priceDiscount", mode="before")
    @classmethod
    def set_price_discount(cls, value, values):
        if value is None:
            price = values.data.get("price")
            discount = values.data.get("discount")

            if price == 0:
                return 0
            # Si discount es None o 0, el precio con descuento es igual al precio original
            if discount is None or discount == 0:
                return 0

            # Si discount es un valor positivo, calcular el precio con descuento
            if discount > 0:
              return price * (1 - discount / 100)

            # En cualquier otro caso, devolver el precio original
            return 0
        return value

class ProductCreate(ProductBaseDTO):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class Product(ProductBaseDTO):
    id: int

    class Config:
        from_attributes = True