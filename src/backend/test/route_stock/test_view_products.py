"""Test view products route."""

import unittest

import requests
from app import app
from flask import json
from services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestViewStock(unittest.TestCase):
    """Test view products route."""

    def test_view_products(self: "TestViewStock") -> None:
        """Test view products route."""
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty("test", 10, 1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = app.test_client().get(url=f"{service.get_stock_url}/{product_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_view_products_fail(self: "TestViewStock") -> None:
        """Fail to view products."""
        response: requests = app.test_client().get(url=f"{service.get_stock_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False

    def test_view_all_products(self: "TestViewStock") -> None:
        """Test view all products route."""
        response: requests = app.test_client().get(url=service.all_stocks_url)
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_view_all_products_fail(self: "TestViewStock") -> None:
        """Fail to view all products."""
        response: requests = app.test_client().get(url=f"{service.all_stocks_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
