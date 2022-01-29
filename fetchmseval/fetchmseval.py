#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
import json
from .download import Download
from .product import Product

ROOT_URL = 'https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022'
DOWNLOAD_LINK_URL = 'https://www.microsoft.com/en-us/evalcenter/umbraco/api/evalcenter/Evaluation?nodeId='


def fetch_products():
    """
    Returns a list of products with their IDs.
    """
    products = []
    r = requests.get(ROOT_URL)

    # Find product IDs
    document = BeautifulSoup(r.text, features="html.parser")
    for link in document.select('#evaluateTopNav .menuContainer ul li a'):
        if not link.get('data-bind'):
            continue

        match = re.search(
            r'evaluateSubNavClick\.bind\(\$data,([0-9]+),', link['data-bind'])
        if match is None:
            print(f"no match {link}")
            continue

        id = match.group(1)
        name = link['aria-label']

        products.append(Product(id, name))

    return products


def fetch_download_urls(product):
    """
    fetch_download_urls

    @type product: Product
    """
    # grab the JSON containing the download links
    download_links_url = f"{DOWNLOAD_LINK_URL}{product.id}"
    r = requests.get(download_links_url)
    download_section_html = r.json()["downloadSectionHTML"]
    document = BeautifulSoup(download_section_html, features="html.parser")
    for input in document.select("input.rbtFileType"):
        routingform = json.loads(input['routingform'])

        for downloadUrl in routingform.get("downloadURLs", []):
            lang = downloadUrl.get('lang', False)
            url = downloadUrl.get('url', '')
            if not lang and re.search(r'\.vhd$', url) is None:
                continue

            if not url:
                continue

            product.downloads.append(Download(url, lang))


def fetch(product_id, language, format):
    product = next(
        (product for product in products if product.id == product_id), None)
    if product is None:
        print(f"Error: unknown product {product_id}")
        return

    fetch_download_urls(product)
