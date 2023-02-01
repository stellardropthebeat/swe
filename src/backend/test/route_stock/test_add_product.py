"""Test add product route."""

import unittest

import requests
from app import app
from flask import json
from services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestAddProduct(unittest.TestCase):
    """Test add product route."""

    def test_add_product(self: "TestAddProduct") -> None:
        """Test add product route."""
        response = service.add_stock("test", 10, 1)
        assert response.status_code == 201

        # Check response data
        response_json: json = response.json()
        assert response_json["success"] is True

    def test_add_product_fail(self: "TestAddProduct") -> None:
        """Fail to add product."""
        fail_test_json = {"name": "test"}
        response: requests = app.test_client().post(url=service.add_stock_url, json=fail_test_json)
        response_json: json = response.json()
        assert response.status_code == 500
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
