import os
import httpx

DELIVERY_SERVICE_URL = "http://localhost:3000/api/v1/deliveries/"


def is_delivery_present(delivery_id: int):
    url = os.environ.get("DELIVERY_SERVICE_URL") or DELIVERY_SERVICE_URL
    r = httpx.get(f"{url}{delivery_id}")
    return True if r.status_code == 200 else False


def get_delivery(delivery_id: int):
    exists = is_delivery_present(delivery_id)
    if exists:
        url = os.environ.get("DELIVERY_SERVICE_URL") or DELIVERY_SERVICE_URL
        return httpx.get(f"{url}{delivery_id}").json()
