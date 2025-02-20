from abc import abstractmethod

from sqlalchemy.orm import Session
from typing import Dict, Optional, List, Type

from app.modules.beauty.domain.models.product import Product
from app.modules.beauty.application.dtos.product.productDTO import ProductCreate


class ProductRepository:
    def __init__(self, db: Session) -> None:
        self.db: Session = db

    @abstractmethod
    def get_product(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    @abstractmethod
    def get_all_products(self) -> List[Type[Product]]:
        return self.db.query(Product).all()

    @abstractmethod
    def create_product(self, product: ProductCreate) -> Product:
        db_product: Product = Product(**product.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    @abstractmethod
    def update_product(self, product_id: int, product_data: Dict[str, str | float | int]) -> Optional[Product]:
        product: Optional[Product] = self.get_product(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product


    @abstractmethod
    def delete_product(self, product_id: int) -> Optional[Product]:
        product: Optional[Product] = self.get_product(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product