# fetchmseval

Download evaluation copies for some MS products straight through your terminal. You can also get them from here via your browser: https://www.microsoft.com/en-us/evalcenter/

## Why?

I just didn't want to go through the MS website everytime I wanted to download a new ISO / VHD to evaluate a product. It also provides some convenience when setting up virtual machines for testing purposes.

## Usage

```
usage: fetch [-h] [--cache | --no-cache] {list,list-formats,download} ...

Fetch evaluation ISO/VHD files from MS eval center.

positional arguments:
  {list,list-formats,download}
    list                List products available for evaluation
    list-formats        List available file formats and languages for a product
    download            Download an evaluation product

options:
  -h, --help            show this help message and exit
  --cache, --no-cache   use --no-cache to skip and refresh the cache ($TEMP_DIR/__fetchmseval.cache.json) (default: True)
```
