"""Test delete product route."""

import unittest

import requests
from app import app
from flask import json
from services.stock_test_services import StockTestServices

service: StockTestServices = StockTestServices()


class TestDeleteProduct(unittest.TestCase):
    """Test delete product route."""

    def test_delete_product(self: "TestDeleteProduct") -> None:
        """Test delete product route."""
        all_products_url: json = service.query_all_stocks()
        if len(all_products_url) == 0:
            product_id: int = service.add_stock_if_empty("test", 10, 1)
        else:
            product_id: int = all_products_url[0]["id"]
        response: requests = app.test_client().delete(url=f"{service.delete_stock_url}/{product_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_delete_product_fail(self: "TestDeleteProduct") -> None:
        """Fail to delete product."""
        response: requests = app.test_client().delete(url=f"{service.delete_stock_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
