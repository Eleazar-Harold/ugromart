import os
import httpx

ORDER_SERVICE_URL = "http://localhost:8002/api/v1/orders/"


def is_order_present(order_id: int):
    url = os.environ.get("ORDER_SERVICE_URL") or ORDER_SERVICE_URL
    r = httpx.get(f"{url}{order_id}")
    return True if r.status_code == 200 else False
