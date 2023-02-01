"""Test add product route."""

import random
import string
import unittest

import requests
from flask import json

from vending_machine.services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestAddProduct(unittest.TestCase):
    """Test add product route."""

    def test_add_product(self: "TestAddProduct") -> None:
        """Test add product route."""
        letters = string.ascii_lowercase
        name: str = "".join(random.choice(letters) for i in range(10))
        response = service.add_stock(vm_id=2, product=name, quantity=1)
        assert response.status_code == 201

        # Check response data
        response_json: json = response.json()
        assert response_json["success"] is True
        # TODO: change to app.test_client().get() to test the route

    def test_add_product_fail(self: "TestAddProduct") -> None:
        """Fail to add product."""
        fail_test_json: json = {"vm_id": 2, "product": "test"}
        response: requests = requests.post(url=service.add_stock_url, json=fail_test_json)
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
