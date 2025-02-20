import uvicorn
from fastapi import FastAPI

from app.modules.beauty.v1.endpoints import product
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI()

app.include_router(product.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)