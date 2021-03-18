import os
import httpx

PRODUCT_SERVICE_URL = "http://localhost:8002/api/v1/products/"


def is_product_present(product_id: int):
    url = os.environ.get("PRODUCT_SERVICE_URL") or PRODUCT_SERVICE_URL
    r = httpx.get(f"{url}{product_id}")
    return True if r.status_code == 200 else False


def get_product(product_id: int):
    exists = is_product_present(product_id)
    if exists:
        url = os.environ.get("PRODUCT_SERVICE_URL") or PRODUCT_SERVICE_URL
        return httpx.get(f"{url}{product_id}").json()
