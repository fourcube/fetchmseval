from .common import initialize_products
from ..cache import from_cache, put_cache
from ..product import print_products, products_list, from_dict as product_from_dict


def cli_list(args):
    products = []
    if args.cache == True:
        products = [product_from_dict(product)
                    for product in from_cache("products", [])]

    if len(products) == 0:
        products = initialize_products()

    print_products(products_list(products))
