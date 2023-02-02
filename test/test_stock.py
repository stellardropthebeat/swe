import secrets
import string

from flask import json

from src.app import app

parser = "html.parser"

add_url: str = "/add_product"
delete_url: str = "/delete_product"
update_url: str = "/update_product"
all_products_url: str = "/all_products"


def random_string(length: int) -> str:
    """Get a random string."""
    rand_str = "".join(secrets.choice(string.ascii_letters) for _ in range(length))
    return rand_str


def get_id() -> int:
    """Get the first product_id found."""
    machines = app.test_client().get(all_products_url).get_json()
    product_id = machines[0]["id"]
    return product_id


def random_json() -> json:
    """Get a random json."""
    vm_id: int = get_id()
    product: str = random_string(5)
    quantity: int = secrets.randbelow(100)
    rand_json = {"vm_id": vm_id, "product": product, "quantity": quantity}
    return json.dumps(rand_json)


def test_add_product() -> None:
    """Test add product route."""
    test_json: json = random_json()
    success: bool = True
    result: json = app.test_client().post(add_url, data=test_json, content_type="application/json").get_json()
    assert success == result["success"]


def test_update_product() -> None:
    """Test update product route."""
    test_json: json = random_json()
    product_id: int = get_id()
    success: bool = True
    result: json = (
        app.test_client().put(f"{update_url}/{product_id}", data=test_json, content_type="application/json").get_json()
    )
    assert success == result["success"]


def test_delete_product() -> None:
    """Test delete product route."""
    product_id: int = get_id()
    success: bool = True
    result: json = app.test_client().delete(f"{delete_url}/{product_id}").get_json()
    assert success == result["success"]


def test_render_stock_page() -> None:
    """Test render stock page."""
    response: int = app.test_client().get("/stock").status_code
    assert response == 200
