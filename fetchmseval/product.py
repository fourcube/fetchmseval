from .printable import Printable
from tabulate import tabulate
from .download import from_dict as download_from_dict, to_dict as download_to_dict


class Product(Printable):
    def __init__(self, id=None, name=None, downloads=[]):
        self.id = int(id)
        self.name = name
        self.downloads = downloads


def from_dict(product):
    return Product(product.get('id', -1), product.get('name', 'unknown'),
                   [download_from_dict(download) for download in product.get('downloads', [])])


def to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "downloads": [download_to_dict(download) for download in product.downloads]
    }


def products_list(products):
    return [[product.name, product.id]
            for product in sorted(products, key=lambda product: product.name)]


def print_products(products_list):
    print(tabulate(products_list, headers=["Product", "ID"]))
