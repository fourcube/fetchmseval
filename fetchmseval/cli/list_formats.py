
from ..product import from_dict as product_from_dict, to_dict as product_to_dict
from ..cache import from_cache, put_cache
from .common import initialize_products
from ..fetchmseval import fetch_download_urls
from ..download import formats_list, print_formats


def cli_list_formats(args):
    product_id = args.product_id
    products = None
    if args.cache == True:
        products = [product_from_dict(product)
                    for product in from_cache("products", [])]

    if len(products) == 0:
        products = initialize_products()

    product = next(
        (product for product in products if product.id == product_id), None)

    if product is None:
        print(f"Error: unknown product {product_id}")
        return

    if len(product.downloads) == 0:
        # TODO: Error handling
        fetch_download_urls(product)
        put_cache("products", [product_to_dict(product)
                  for product in products])

    formats = formats_list(product.downloads)
    print(f"{product.name} is available in the following formats:")
    print_formats(formats)
