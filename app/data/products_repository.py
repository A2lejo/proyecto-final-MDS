from app.models.models import Product, ProductCreate

products: list[Product] = [
    Product(id=1, name="Laptop", description="Equipo portátil para oficina", stock=8, price=1250.0),
    Product(id=2, name="Mouse", description="Mouse inalámbrico", stock=24, price=18.5),
]
next_id = len(products) + 1


def get_all_products():
    return products


def create_product(product_data: ProductCreate):
    global next_id
    product = Product(
        id=next_id,
        name=product_data.name,
        description=product_data.description,
        stock=product_data.stock,
        price=product_data.price,
    )
    products.append(product)
    next_id += 1
    return product


def update_stock(product_id: int, stock: int):
    for product in products:
        if product.id == product_id:
            product.stock = stock
            return product
    return None
