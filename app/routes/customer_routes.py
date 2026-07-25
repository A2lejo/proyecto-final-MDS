from fastapi import APIRouter

from app.models.models import CustomerCreate
from app.services.customer_service import disable_customer, list_customers, register_customer
from app.utils.logger import logger
from app.utils.validators import validate_exists

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("")
def get_customers():
    logger.info("Listing all customers")
    return list_customers()


@router.post("")
def create_customer_endpoint(data: CustomerCreate):
    customer = register_customer(data)
    logger.info(f"Cliente registrado: {customer.email}")
    return customer


@router.put("/{customer_id}/deactivate")
def deactivate(customer_id: int):
    customer = disable_customer(customer_id)
    customer = validate_exists(customer, "Cliente no encontrado")
    logger.info(f"Cliente desactivado: {customer.email}")
    return customer
