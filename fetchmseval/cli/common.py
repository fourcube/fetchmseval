from ..cache import put_cache
from ..product import to_dict as product_to_dict
from ..fetchmseval import fetch_products


def initialize_products():
    products = fetch_products()
    put_cache("products", [product_to_dict(product) for product in products])
    return products
