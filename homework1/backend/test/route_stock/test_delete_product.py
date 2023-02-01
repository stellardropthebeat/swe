"""Test delete product route."""

import unittest

import requests
from flask import json
from services.test_stock_services import TestStockServices

service: TestStockServices = TestStockServices()


class TestDeleteProduct(unittest.TestCase):
    """Test delete product route."""

    def test_delete_product(self: "TestDeleteProduct") -> None:
        """Test delete product route."""
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty("test", 10, 1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = requests.delete(url=f"{service.delete_stock_url}/{product_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_delete_product_fail(self: "TestDeleteProduct") -> None:
        """Fail to delete product."""
        response: requests = requests.delete(url=f"{service.delete_stock_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
