import secrets
import string

from app import app
from bs4 import BeautifulSoup
from flask import json
from services.stock_services import StockManager

parser = "html.parser"

add_url: str = "/add_product"
delete_url: str = "/delete_product"
update_url: str = "/update_product"
all_products_url: str = "/all_products"

service = StockManager()


def random_string(length: int) -> str:
    """Get a random string."""
    rand_str = "".join(secrets.choice(string.ascii_letters) for _ in range(length))
    return rand_str


def random_json() -> dict:
    """Get a random json."""
    vm_id: int = service.get_random_id()
    product: str = random_string(5)
    quantity: int = secrets.randbelow(100)
    rand_json = {"vm_id": vm_id, "product": product, "quantity": quantity}
    return rand_json


def test_add_product() -> None:
    """Test add product route."""
    test_json: json = random_json()
    product: str = test_json["product"]
    app.test_client().post(add_url, data=test_json)

    products = app.test_client().get(all_products_url).data
    soup = BeautifulSoup(products, parser)
    assert product == soup.find(text=product)


def test_delete_product() -> None:
    """Test delete product route."""
    product_id: int = service.get_random_id()
    app.test_client().post(f"{delete_url}/{product_id}")

    products = app.test_client().get(all_products_url).data
    soup = BeautifulSoup(products, parser)
    assert soup.find("a", {"id": product_id}) is None
