from fastapi import FastAPI

from app.api.v1.endpoints import product
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI()

app.include_router(product.router, prefix="/api/v1")