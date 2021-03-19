import os
import httpx

VARIATION_SERVICE_URL = "http://localhost:6006/api/v1/variations/"
PRODUCT_SERVICE_URL = "http://localhost:6000/api/v1/products/"


def is_variation_present(variation_id: int):
    url = os.environ.get("VARIATION_SERVICE_URL") or VARIATION_SERVICE_URL
    r = httpx.get(f"{url}{variation_id}")
    return True if r.status_code == 200 else False


def is_product_present(product_id: int):
    url = os.environ.get("PRODUCT_SERVICE_URL") or PRODUCT_SERVICE_URL
    r = httpx.get(f"{url}{product_id}")
    return True if r.status_code == 200 else False


def get_variation(variation_id: int):
    exists = is_variation_present(variation_id)
    if exists:
        url = os.environ.get("VARIATION_SERVICE_URL") or VARIATION_SERVICE_URL
        return httpx.get(f"{url}{variation_id}").json()


def get_product(product_id: int):
    exists = is_product_present(product_id)
    if exists:
        url = os.environ.get("PRODUCT_SERVICE_URL") or PRODUCT_SERVICE_URL
        return httpx.get(f"{url}{product_id}").json()
