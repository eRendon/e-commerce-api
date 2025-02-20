from typing import Dict, Optional, List, Type

from app.modules.beauty.domain.repositories.product_repository import ProductRepository
from app.modules.beauty.application.dtos.product.productDTO import ProductCreate, Product


class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository: ProductRepository = product_repository

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.product_repository.get_product(product_id)

    def get_all_products(self) -> List[Type[Product]]:
        return self.product_repository.get_all_products()

    def create_product(self, product: ProductCreate) -> Product:
        return self.product_repository.create_product(product)

    def update_product(self, product_id: int, product_data: Dict[str, str | float | int]) -> Optional[Product]:
        return self.product_repository.update_product(product_id, product_data)

    def delete_product(self, product_id: int) -> Optional[Product]:
        return self.product_repository.delete_product(product_id)