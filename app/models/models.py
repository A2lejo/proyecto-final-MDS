from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    stock: int = 0
    price: float | None = None


class Product(BaseModel):
    id: int
    name: str
    description: str | None = None
    stock: int = 0
    price: float | None = None


class CustomerCreate(BaseModel):
    name: str
    email: str


class Customer(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True
