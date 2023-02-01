"""Test update machine route."""

import unittest

import requests
from flask import json

from vending_machine.services.vm_test_services import VendingTestServices

service: VendingTestServices = VendingTestServices()


class TestUpdateMachine(unittest.TestCase):
    """Test update machine route."""

    def test_update_machine(self: "TestUpdateMachine") -> None:
        """Test update machine route."""
        test_json: json = {"name": "test", "location": "test"}
        all_machines_url: json = service.query_all_machines()
        if len(all_machines_url) == 0:
            machine_id: int = service.add_machine_if_empty("test", "test")
        else:
            machine_id: int = all_machines_url[0]["id"]
        response: requests = requests.put(url=f"{service.update_machine_url}/{machine_id}", json=test_json)
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_update_machine_fail(self: "TestUpdateMachine") -> None:
        """Fail to delete machine."""
        response: requests = requests.put(url=f"{service.update_machine_url}/0")
        assert response.status_code == 400


if __name__ == "__main__":
    unittest.main()
