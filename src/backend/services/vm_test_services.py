"""Test Vending Machine services."""

import requests
from app import app
from flask import json


class VendingTestServices:
    """Test services."""

    def __init__(self: "VendingTestServices") -> None:
        """Initialize test services."""
        self.endpoint: str = "http://localhost:5001"
        self.all_machines_url: str = f"{self.endpoint}/all_machines"
        self.add_machine_url: str = f"{self.endpoint}/add_machine"
        self.get_machine_url: str = f"{self.endpoint}/get_machine"
        self.update_machine_url: str = f"{self.endpoint}/update_machine"
        self.delete_machine_url: str = f"{self.endpoint}/delete_machine"

    def query_all_machines(self: "VendingTestServices") -> json:
        """Query all machines."""
        all_machines: json = app.test_client().get(self.all_machines_url).json()
        return all_machines

    def add_machine(self: "VendingTestServices", name: str, location: str) -> requests:
        """Add machine."""
        test_json: json = {"name": name, "location": location}
        response: requests = app.test_client().get(self.all_machines_url, data=test_json)
        return response

    def add_machine_if_empty(self: "VendingTestServices", name: str, location: str) -> json:
        """Add machine if empty."""
        machine_id: int = 0
        if len(self.query_all_machines()) == 0:
            machine_id: int = self.add_machine(name, location).json()["id"]
        return machine_id
