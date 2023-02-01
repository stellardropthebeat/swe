"""Test view products route."""

import unittest

import requests
from flask import json

from services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestViewStock(unittest.TestCase):
    """Test view products route."""

    def test_view_products(self: "TestViewStock") -> None:
        """Test view products route."""
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty(vm_id=1, product="test", quantity=1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = requests.get(url=f"{service.get_stock_url}/{product_id}")
        assert response.status_code == 200

    def test_view_products_fail(self: "TestViewStock") -> None:
        """Fail to view products."""
        response: requests = requests.get(url=f"{service.get_stock_url}/0")
        assert response.status_code == 404

    def test_view_all_products(self: "TestViewStock") -> None:
        """Test view all products route."""
        response: requests = requests.get(url=f"{service.all_stocks_url}")
        assert response.status_code == 200

    def test_view_all_products_fail(self: "TestViewStock") -> None:
        """Fail to view all products."""
        response: requests = requests.get(url=f"{service.all_stocks_url}/0")
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
