"""Test delete product route."""

import unittest

import requests
from flask import json
from services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestDeleteProduct(unittest.TestCase):
    """Test delete product route."""

    def test_delete_product(self: "TestDeleteProduct") -> None:
        """Test delete product route."""
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty(vm_id=2, product="test", quantity=1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = requests.delete(url=f"{service.delete_stock_url}/{product_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_delete_product_fail(self: "TestDeleteProduct") -> None:
        """Fail to delete product."""
        response: requests = requests.delete(url=f"{service.delete_stock_url}/0")
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
