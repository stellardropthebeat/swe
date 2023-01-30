"""Test delete machine route."""

import unittest

import requests
from flask import json

ENDPOINT: str = "http://localhost:5001"

delete_machine_url: str = f"{ENDPOINT}/delete_machine"
all_machines_url: json = requests.get(f"{ENDPOINT}/all_machines").json()


class TestDeleteMachine(unittest.TestCase):
    """Test delete machine route."""

    def test_delete_machine(self: "TestDeleteMachine") -> None:
        """Test delete machine route."""
        if len(all_machines_url) == 0:
            add_machine_url: str = f"{ENDPOINT}/add_machine"
            test_json: json = {"name": "test", "location": "test"}
            response: requests = requests.post(url=add_machine_url, json=test_json)
            response_json: json = response.json()
            machine_id: int = response_json["id"]
        else:
            machine_id: int = all_machines_url[0]["id"]
        response: requests = requests.delete(url=f"{delete_machine_url}/{machine_id}")
        assert response.status_code == 200

    def test_delete_machine_fail(self: "TestDeleteMachine") -> None:
        """Fail to delete machine."""
        response: requests = requests.delete(url=f"{delete_machine_url}/-1")
        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
