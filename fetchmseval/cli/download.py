import requests
import os
from ..product import from_dict as product_from_dict, to_dict as product_to_dict
from ..cache import from_cache, put_cache
from .common import initialize_products
from ..fetchmseval import fetch_download_urls
from tqdm import tqdm


def cli_download(args):
    product_id = args.product_id
    language = args.language
    fmt = args.format
    resume = args.resume

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

    download = next(
        (download for download in product.downloads if (language == '' or download.language.lower() == language.lower()) and download.format.lower() == fmt.lower()), None)

    if download is None:
        print(f"Error: download unavailable for {product_id} {language} {fmt}")
        return

    print(
        f"Downloading {product.name} ({fmt}) for language '{download.language}' to '{download.filename}'")

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    if resume:
        try:
            stat = os.stat(download.filename)
            headers['range'] = f"{stat.st_size}-"
        except:
            print(f"{download.filename} does not exist. Downloading.")

    r = requests.get(download.url, stream=True, headers=headers)

    try:
        with tqdm.wrapattr(open(download.filename, 'wb+'), 'write',
                           miniters=1,
                           desc=download.filename,
                           total=int(r.headers.get('content-length', 0))) as fd:

            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

        print("Done!")
    except e:
        print("Failed to download", e)
