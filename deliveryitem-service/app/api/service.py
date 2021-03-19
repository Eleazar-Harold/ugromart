import os
import httpx

DELIVERY_SERVICE_URL = "http://localhost:3000/api/v1/deliveries/"
PRODUCTITEM_SERVICE_URL = "http://localhost:6004/api/v1/productitems/"
UOM_SERVICE_URL = "http://localhost:7000/api/v1/unitofmeasures/"


def is_delivery_present(delivery_id: int):
    url = os.environ.get("DELIVERY_SERVICE_URL") or DELIVERY_SERVICE_URL
    r = httpx.get(f"{url}{delivery_id}")
    return True if r.status_code == 200 else False


def get_delivery(delivery_id: int):
    exists = is_delivery_present(delivery_id)
    if exists:
        url = os.environ.get("DELIVERY_SERVICE_URL") or DELIVERY_SERVICE_URL
        return httpx.get(f"{url}{delivery_id}").json()


def is_productitem_present(productitem_id: int):
    url = os.environ.get("PRODUCTITEM_SERVICE_URL") or PRODUCTITEM_SERVICE_URL
    r = httpx.get(f"{url}{productitem_id}")
    return True if r.status_code == 200 else False


def get_productitem(productitem_id: int):
    exists = is_productitem_present(productitem_id)
    if exists:
        url = os.environ.get("PRODUCTITEM_SERVICE_URL") or PRODUCTITEM_SERVICE_URL
        return httpx.get(f"{url}{productitem_id}").json()


def is_uom_present(uom_id: int):
    url = os.environ.get("UOM_SERVICE_URL") or UOM_SERVICE_URL
    r = httpx.get(f"{url}{uom_id}")
    return True if r.status_code == 200 else False


def get_uom(uom_id: int):
    exists = is_uom_present(uom_id)
    if exists:
        url = os.environ.get("UOM_SERVICE_URL") or UOM_SERVICE_URL
        return httpx.get(f"{url}{uom_id}").json()
