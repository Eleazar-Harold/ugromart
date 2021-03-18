import os
import httpx

ORDER_SERVICE_URL = "http://localhost:8002/api/v1/orders/"
PRODUCTITEM_SERVICE_URL = "http://localhost:8002/api/v1/productitems/"
UOM_SERVICE_URL = "http://localhost:8002/api/v1/unitofmeasures/"


def is_order_present(order_id: int):
    url = os.environ.get("ORDER_SERVICE_URL") or ORDER_SERVICE_URL
    r = httpx.get(f"{url}{order_id}")
    return True if r.status_code == 200 else False


def is_productitem_present(productitem_id: int):
    url = os.environ.get("PRODUCTITEM_SERVICE_URL") or PRODUCTITEM_SERVICE_URL
    r = httpx.get(f"{url}{productitem_id}")
    return True if r.status_code == 200 else False


def is_uom_present(uom_id: int):
    url = os.environ.get("UOM_SERVICE_URL") or UOM_SERVICE_URL
    r = httpx.get(f"{url}{uom_id}")
    return True if r.status_code == 200 else False
