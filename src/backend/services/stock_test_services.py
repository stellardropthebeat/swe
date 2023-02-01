"""Test Stock services."""

import requests
from flask import json


class StockTestServices:
    """Test services."""

    def __init__(self: "StockTestServices") -> None:
        """Initialize test services."""
        self.endpoint: str = "http://localhost:5001"
        self.all_stocks_url: str = f"{self.endpoint}/all_products"
        self.add_stock_url: str = f"{self.endpoint}/add_product"
        self.get_stock_url: str = f"{self.endpoint}/get_product"
        self.update_stock_url: str = f"{self.endpoint}/update_product"
        self.delete_stock_url: str = f"{self.endpoint}/delete_product"

    def query_all_stocks(self: "StockTestServices") -> json:
        """Query all stocks."""
        all_stocks: json = requests.get(self.all_stocks_url).json()
        return all_stocks

    def add_stock(self: "StockTestServices", name: str, price: int, quantity: int) -> requests:
        """Add stock."""
        test_json: json = {"name": name, "price": price, "quantity": quantity}
        response: requests = requests.post(url=self.add_stock_url, json=test_json)
        return response

    def add_stock_if_empty(self: "StockTestServices", name: str, price: int, quantity: int) -> json:
        """Add stock if empty."""
        stock_id: int = 0
        if len(self.query_all_stocks()) == 0:
            stock_id: int = self.add_stock(name, price, quantity).json()["id"]
        return stock_id
