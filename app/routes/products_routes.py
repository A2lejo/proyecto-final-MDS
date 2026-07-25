from fastapi import APIRouter
from pydantic import BaseModel

from app.models.models import ProductCreate
from app.services.products_service import change_stock, list_products, register_product
from app.utils.validators import validate_exists

router = APIRouter(prefix="/products", tags=["Products"])


class StockUpdate(BaseModel):
    stock: int


@router.get("")
def get_products():
    return list_products()


@router.post("")
def create_product_endpoint(data: ProductCreate):
    return register_product(data)


@router.put("/{product_id}/stock")
def update_stock_endpoint(product_id: int, data: StockUpdate):
    product = change_stock(product_id, data.stock)
    return validate_exists(product, "Producto no encontrado")
