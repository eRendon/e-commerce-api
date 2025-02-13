from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Type

from app.api.domain.repositories.product_repository import ProductRepository
from app.api.domain.schemas.product import ProductCreate, ProductUpdate, Product
from app.api.domain.services.product_service import ProductService
from app.db.session import get_db

router: APIRouter = APIRouter()

@router.post("/products/", response_model=Product)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> Product | None:
    product_repository: ProductRepository = ProductRepository(db)
    product_service: ProductService = ProductService(product_repository)
    return product_service.create_product(product)

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    product_repository: ProductRepository = ProductRepository(db)
    product_service: ProductService = ProductService(product_repository)
    product: Optional[Product] = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/products/", response_model=list[Product])
def read_all_products(db: Session = Depends(get_db)) -> List[Type[Product]]:
    product_repository: ProductRepository = ProductRepository(db)
    product_service: ProductService = ProductService(product_repository)
    return product_service.get_all_products()

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)) -> Product:
    product_repository: ProductRepository = ProductRepository(db)
    product_service: ProductService = ProductService(product_repository)
    updated_product: Optional[Product] = product_service.update_product(product_id, product.model_dump())
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)) -> Dict[str, str]:
    product_repository: ProductRepository = ProductRepository(db)
    product_service: ProductService = ProductService(product_repository)
    deleted_product: Optional[Product] = product_service.delete_product(product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}