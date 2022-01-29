import tempfile
import json
from os import stat, unlink
from pathlib import Path

tmp_dir = tempfile.gettempdir()
CACHE_FILENAME = "__fetchmseval.cache.json"
CURRENT_VERSION = "0.1"


def load_cache():
    # TODO: check version
    cache_path = Path(tmp_dir, CACHE_FILENAME).resolve()

    try:
        with open(cache_path, 'r') as cache_fp:
            return json.load(cache_fp)
    except IOError:
        return {
            "version": CURRENT_VERSION
        }


def save_cache(data):
    cache_path = Path(tmp_dir, CACHE_FILENAME).resolve()

    try:
        with open(cache_path, 'w') as cache_fp:
            json.dump(data, cache_fp)
    except IOError as e:
        # delete the cache, it is probably corrupted by a partial write
        unlink(cache_path)
        print(f"Failed to cache data {e}")


def put_cache(key, result):
    cache = load_cache()
    cache[key] = result
    save_cache(cache)


def from_cache(key, default=None):
    cache = load_cache()
    return cache.get(key, default)
