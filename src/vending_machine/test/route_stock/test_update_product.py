"""Test Update Product route."""

import unittest

import requests
from flask import json

from vending_machine.services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestUpdateProduct(unittest.TestCase):
    """Test Update Product route."""

    def test_update_product(self: "TestUpdateProduct") -> None:
        """Test Update Product route."""
        test_json: json = {"vm_id": 2, "product": "test", "quantity": 1}
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty(vm_id=1, product="test", quantity=1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = requests.put(url=f"{service.update_stock_url}/{product_id}", json=test_json)
        assert response.status_code == 200

        # Check response data
        response_json: json = response.json()
        assert response_json["success"] is True

    def test_update_product_fail(self: "TestUpdateProduct") -> None:
        """Fail to Update Product."""
        fail_test_json = {"name": "test"}
        response: requests = requests.put(url=f"{service.update_stock_url}/0", json=fail_test_json)
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
