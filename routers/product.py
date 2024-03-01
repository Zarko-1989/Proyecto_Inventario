from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from models.product import Product as ProductModel
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.product import ProductService
from schemas.product import Product

product_router = APIRouter()


@product_router.get("/product", tags=['product'], response_model=List[Product],
                  status_code=200, dependencies=[Depends(JWTBearer())])
def get_products() -> List[Product]:
    result = ProductService(Session()).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.get("/product/{id}", tags=['product'], response_model=Product, status_code=200)
# se cambia y se dice que es igual a Path(int)
def get_product(id: int = Path(ge=1, le=2000)) -> Product:
    result = ProductService(Session()).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={
            "message": "Product not found"
            })
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.get("/product/", tags=['product'], response_model=List[Product])
def get_products_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Product]:
    result = ProductService(Session()).get_products_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Products not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.post("/product", tags=['product'], response_model=dict, status_code=201)
def create_product(product: Product) -> dict:
    ProductService(Session()).create_product(product)
    return JSONResponse(content={"message": "Product created successfully"}, status_code=201)


@product_router.put("/product/{id}", tags=['product'], response_model=dict, status_code=200)
def update_product(id: int, product: Product) -> dict:
    if not ProductService(Session()).get_product(id):
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    ProductService(ProductService(Session()).get_product(id)).update_product(id, product)
    return JSONResponse(content={"message": "Product updated successfully"}, status_code=200)


@product_router.delete("/product/{id}", tags=['product'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_product(id: int) -> dict:
    if not ProductService(Session()).get_product(id):
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    ProductService(Session()).delete_product(id)
    return JSONResponse(content={"message": "Product deleted successfully"})