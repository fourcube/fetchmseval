from .printable import Printable
from tabulate import tabulate
import re
import os
from urllib.parse import urlparse


def _determine_file_format(url):
    """
    Checks the suffix of a url and returns the everything
    after the last '.' character.
    """
    if re.search(r'\.iso$', url) is not None:
        return 'iso'
    elif re.search(r'\.vhd$', url) is not None:
        return 'vhd'

    m = re.search(r'\.(.*)$', url)
    if m is not None:
        return m.group(1)


class Download(Printable):
    def __init__(self, url=None, language='ALL', format=''):
        self.url = url
        self.language = language or 'ALL'
        self.format = _determine_file_format(url)
        self.filename = os.path.basename(urlparse(url).path)


def from_dict(download):
    return Download(download.get('url', 'url not avaialble'), download.get('language', 'language not available'), download.get('format', 'format not available'))


def to_dict(download):
    return {
        "url": download.url,
        "language": download.language,
        "format": download.format
    }


def formats_list(downloads):
    return [[download.language, download.format]
            for download in sorted(downloads, key=lambda download: download.language)]


def print_formats(download_list):
    print(tabulate(download_list, headers=["Language", "Format"]))
