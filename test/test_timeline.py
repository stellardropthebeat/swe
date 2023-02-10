"""Test the timeline module."""

from src.app import app
from src.database.model import Stock, StockTimeLine, add_to_timeline

stock_timeline_url: str = "/stock_timeline/product"
vm_timeline_url: str = "/stock_timeline/vm"
all_products_url: str = "/all_products"
all_machines_url: str = "/all_machines"


def get_id() -> int:
    """Get the first product_id found."""
    products = app.test_client().get(all_products_url).get_json()
    product_id = products[0]["id"]
    return product_id


def get_vm_id() -> int:
    """Get the first vm_id found."""
    machines = app.test_client().get(all_machines_url).get_json()
    vm_id = machines[0]["id"]
    return vm_id


def test_add_to_timeline_model() -> None:
    """Test add to timeline model."""
    add_to_timeline(1, 1, 1)
    assert isinstance(StockTimeLine.query.filter_by(product_id=1).first(), StockTimeLine)


def test_get_all_product_stock_model() -> None:
    """Test get all product stock model."""
    stock_timeline: StockTimeLine = StockTimeLine.query.filter_by(product_id=1).first()
    ret: dict = StockTimeLine.get_all_product_stock(stock_timeline)
    assert isinstance(ret, dict)


def test_add_product_to_timeline() -> None:
    """Test add product to timeline."""
    product_id: int = get_id()
    with app.test_client() as client:
        response = client.get(f"{stock_timeline_url}/{product_id}")
        assert response.status_code == 200
        assert response.json[1]["product_name"] == Stock.query.filter_by(id=product_id).first().product


def test_get_stock_timeline_by_vm() -> None:
    """Test get stock timeline by vm."""
    vm_id: int = get_vm_id()
    with app.test_client() as client:
        response = client.get(f"{vm_timeline_url}/{vm_id}")
        assert response.status_code == 200
