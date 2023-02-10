"""Test the timeline module."""
from flask import Response

from src.app import app
from src.database.model import add_to_timeline, StockTimeLine
from src.database.model import StockTimeLine, Stock
from src.services.stock_services import StockManager

stock_timeline_url: str = "/stock_timeline/product"
vm_timeline_url: str = "/stock_timeline/vm"


def test_add_to_timeline_model() -> None:
    """Test add to timeline model."""
    add_to_timeline(1, 1, 1)
    assert StockTimeLine.query.filter_by(vm_id=1, product_id=1, quantity=1).first() is not None


def test_get_all_product_stock_model() -> None:
    """Test get all product stock model."""
    stock_timeline: StockTimeLine = StockTimeLine.query.filter_by(product_id=1).first()
    ret: dict = StockTimeLine.get_all_product_stock(stock_timeline)
    assert ret["product_name"] == Stock.query.filter_by(id=1).first().product


def test_add_product_to_timeline() -> None:
    """Test add product to timeline."""
    stock_manager: StockManager = StockManager()
    product_id: int = stock_manager.get_random_id()
    with app.test_client() as client:
        response = client.get(f"{stock_timeline_url}/{product_id}")
        assert response.status_code == 200
        assert response.json[1]["product_name"] == Stock.query.filter_by(id=product_id).first().product


def test_get_stock_timeline_by_vm() -> None:
    """Test get stock timeline by vm."""
    stock_manager: StockManager = StockManager()
    vm_id: int = stock_manager.get_random_id()
    with app.test_client() as client:
        response = client.get(f"{vm_timeline_url}/{vm_id}")
        assert response.status_code == 200
