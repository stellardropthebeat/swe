"""Test add product route."""

import unittest

import requests
from flask import json
from services.test_stock_services import TestStockServices

service: TestStockServices = TestStockServices()


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
        response: requests = requests.post(url=service.add_stock_url, json=fail_test_json)
        response_json: json = response.json()
        assert response.status_code == 500
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
